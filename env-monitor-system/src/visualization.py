import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class DataVisualizer:
    """数据可视化器"""

    def __init__(self, data):
        self.data = data

    def plot_time_series(self, save_path='docs/timeseries.png'):
        """绘制时间序列图"""
        fig, axes = plt.subplots(3, 1, figsize=(12, 10))

        # 温度趋势
        axes[0].plot(self.data['date'], self.data['temperature'], marker='o', color='red')
        axes[0].set_title('温度变化趋势')
        axes[0].set_ylabel('温度(℃)')
        axes[0].grid(True)

        # 湿度趋势
        axes[1].plot(self.data['date'], self.data['humidity'], marker='s', color='blue')
        axes[1].set_title('湿度变化趋势')
        axes[1].set_ylabel('湿度(%)')
        axes[1].grid(True)

        # PM2.5趋势
        axes[2].plot(self.data['date'], self.data['pm25'], marker='^', color='green')
        axes[2].set_title('PM2.5变化趋势')
        axes[2].set_ylabel('PM2.5(μg/m³)')
        axes[2].set_xlabel('日期')
        axes[2].grid(True)
        axes[2].axhline(y=75, color='orange', linestyle='--', label='良/轻度污染界线')
        axes[2].legend()

        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"时间序列图已保存到 {save_path}")
        plt.show()

    def plot_distribution(self, save_path='docs/distribution.png'):
        """绘制数据分布图"""
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))

        # 温度分布
        axes[0, 0].hist(self.data['temperature'], bins=10, color='red', alpha=0.7)
        axes[0, 0].set_title('温度分布')
        axes[0, 0].set_xlabel('温度(℃)')

        # 湿度分布
        axes[0, 1].hist(self.data['humidity'], bins=10, color='blue', alpha=0.7)
        axes[0, 1].set_title('湿度分布')
        axes[0, 1].set_xlabel('湿度(%)')

        # PM2.5分布
        axes[1, 0].hist(self.data['pm25'], bins=10, color='green', alpha=0.7)
        axes[1, 0].set_title('PM2.5分布')
        axes[1, 0].set_xlabel('PM2.5(μg/m³)')
        axes[1, 0].axvline(x=75, color='orange', linestyle='--', label='良/轻度污染界线')
        axes[1, 0].legend()

        # 站点对比
        location_avg = self.data.groupby('location')[['temperature', 'humidity', 'pm25']].mean()
        x = range(len(location_avg))
        width = 0.25
        axes[1, 1].bar([i - width for i in x], location_avg['temperature'], width, label='温度', color='red')
        axes[1, 1].bar(x, location_avg['humidity'], width, label='湿度', color='blue')
        axes[1, 1].bar([i + width for i in x], location_avg['pm25']/5, width, label='PM2.5/5', color='green')
        axes[1, 1].set_title('站点指标对比')
        axes[1, 1].set_xticks(x)
        axes[1, 1].set_xticklabels(location_avg.index)
        axes[1, 1].legend()

        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"分布图已保存到 {save_path}")
        plt.show()

    def plot_correlation(self, save_path='docs/correlation.png'):
        """绘制相关性热图"""
        corr = self.data[['temperature', 'humidity', 'pm25']].corr()

        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', center=0,
                    square=True, linewidths=1)
        plt.title('环境指标相关性分析')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"相关性热图已保存到 {save_path}")
        plt.show()

# 测试代码
if __name__ == '__main__':
    from data_loader import DataLoader

    loader = DataLoader()
    data = loader.load_data()

    visualizer = DataVisualizer(data)
    visualizer.plot_time_series()
    visualizer.plot_distribution()
    visualizer.plot_correlation()