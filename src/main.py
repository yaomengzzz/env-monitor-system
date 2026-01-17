"""
环境监测数据分析系统 - 主程序
"""

from data_loader import DataLoader
from data_analysis import DataAnalyzer
from visualization import DataVisualizer

def main():
    print("="*50)
    print("      环境监测数据分析系统")
    print("="*50)

    # 1. 加载数据
    print("\n[1] 加载数据...")
    loader = DataLoader()
    data = loader.load_data()
    summary = loader.get_summary()
    print(f"数据形状: {summary['shape']}")
    print(f"日期范围: {summary['date_range'][0]} 至 {summary['date_range'][1]}")
    print(f"监测站点: {summary['locations']}")

    # 2. 数据分析
    print("\n[2] 数据分析...")
    analyzer = DataAnalyzer(data)

    print("\n基础统计:")
    print(analyzer.basic_statistics())

    print("\n站点对比:")
    print(analyzer.location_analysis())

    print("\n空气质量评估:")
    aq_result = analyzer.air_quality_assessment()
    print(f"空气质量分布: {aq_result['quality_distribution'].to_dict()}")
    print(f"优良天数比例: {aq_result['good_days_ratio']}")

    print("\n温度分析:")
    print(analyzer.temperature_extremes())

    # 3. 数据可视化
    print("\n[3] 生成可视化报告...")
    visualizer = DataVisualizer(data)
    visualizer.plot_time_series()
    visualizer.plot_distribution()
    visualizer.plot_correlation()

    print("\n分析完成！")

if __name__ == '__main__':
    main()