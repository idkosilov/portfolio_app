import copy
from datetime import timedelta

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pypfopt import plotting
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.expected_returns import mean_historical_return
from pypfopt.plotting import plot_covariance, plot_weights


class PortfolioOptimizer:

    def __init__(self,
                 data_file,
                 window_size,
                 current_date,
                 risk):
        self.data = pd.read_csv(data_file, index_col='Date', parse_dates=True).sort_values(by='Date')
        self.data.index = pd.to_datetime(self.data.index)
        self.window_size = window_size
        self.current_date = current_date
        self.risk = risk

    def optimize(self):
        start_date = (self.current_date - timedelta(days=self.window_size)).strftime("%Y-%m-%d")
        end_date = self.current_date.strftime("%Y-%m-%d")
        window_data = self.data[start_date: end_date]
        window_data = window_data.dropna(axis=0, how='all')
        window_data = window_data.dropna(how='all', thresh=2)
        window_data = window_data.interpolate(method='pad')
        daily_returns = window_data.pct_change(1)
        covariance_factor = daily_returns.cov()['MOEX.ME']
        variance_factor = daily_returns.var()['MOEX.ME']
        beta = covariance_factor / variance_factor
        alpha = daily_returns.mean() - beta * daily_returns['MOEX.ME'].mean()
        sse_error = (daily_returns - alpha - np.matrix(daily_returns['MOEX.ME']).T @ np.matrix(beta)).std()
        beta_matrix = np.matrix(beta).T @ np.matrix(beta)
        x = np.diag(np.diag(beta_matrix))
        beta_matrix += x @ np.diag(covariance_factor)
        beta_matrix += np.diag(sse_error)
        covariance_matrix = pd.DataFrame(beta_matrix, index=window_data.columns, columns=window_data.columns)
        covariance_matrix = covariance_matrix.drop(index="MOEX.ME", axis=1)
        covariance_matrix = covariance_matrix.drop(columns=["MOEX.ME"], axis=0)
        covariance_matrix = covariance_matrix.dropna(axis=0, how='all')
        covariance_matrix = covariance_matrix.dropna(axis=1, how='all')

        expected_returns = mean_historical_return(window_data,
                                                  frequency=window_data.shape[0]).filter(items=covariance_matrix.index)

        efficient_frontier = EfficientFrontier(expected_returns, covariance_matrix, weight_bounds=(0, 1))

        fig, ax = plt.subplots()
        ef = copy.deepcopy(efficient_frontier)
        plotting.plot_efficient_frontier(ef, ax=ax, show_assets=False)

        # Find the tangency portfolio
        efficient_frontier.efficient_risk(self.risk)
        ret_tangent, std_tangent, _ = efficient_frontier.portfolio_performance()
        ax.scatter(std_tangent, ret_tangent, marker="*", s=100, c="r", label="Эффективный портфель")

        ax.set_title("Efficient Frontier with random portfolios")
        ax.legend()
        plt.tight_layout()
        plt.savefig("ef_scatter.png", dpi=100)

        fig, ax = plt.subplots()
        plot_covariance(covariance_matrix, ax=ax, show_tickers=False)
        plt.savefig("covariance.png", dpi=100)

        weights = efficient_frontier.clean_weights()

        new_weights = {key: value for key, value in weights.items() if value > 0.02}

        fig, ax = plt.subplots()
        plot_weights(new_weights, ax=ax)
        plt.savefig("assets.png", dpi=100)

        return weights, ret_tangent, std_tangent

    def tickers(self):
        return self.data.columns
