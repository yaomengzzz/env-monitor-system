这是一个用于分析环境传感器数据的Python项目，提供数据加载、清洗、分析和可视化功能，帮助用户监测和评估环境质量。

主要功能

📊 数据加载与清洗：支持CSV格式传感器数据加载，自动处理缺失值和异常值

🔍 空气质量评估：根据PM2.5浓度自动评估空气质量等级（优/良/污染）

📈 时间序列分析：可视化温度、湿度、PM2.5随时间变化趋势

🌡️ 多站点对比：比较不同监测站点的环境指标差异
# 1. 将 README.md 添加到暂存区
git add README.md

# 2. 提交到本地仓库
git commit -m “添加项目README文档”

# 3. 推送到远程GitHub仓库的main分支
git push origin main

📝 报告生成：自动生成数据分析报告和可视化图表

快速开始
环境配置
bash
复制
# 克隆仓库
git clone https://github.com/yaomengzzz/env-monitor-system.git
cd env-monitor-system

# 创建Python环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# 安装依赖
pip install -r requirements.txt
运行系统
bash
复制
# 运行主程序
python src/main.py

# 生成模拟数据（可选）
python data/generate_data.py
查看结果

生成的报告和图表位于 docs/目录：

数据分析报告：report.md

时间序列图：timeseries.png

数据分布图：distribution.png

项目结构
复制
env-monitor-system/
├── data/                  # 数据文件
│   ├── sensor_data.csv    # 示例数据
│   └── generate_data.py   # 数据生成脚本
├── src/                   # 源代码
│   ├── data_loader.py     # 数据加载模块
│   ├── data_analysis.py   # 数据分析模块
│   ├── visualization.py   # 可视化模块
│   └── main.py            # 主程序
├── docs/                  # 文档与报告
│   ├── report.md          # 分析报告模板
│   └── timeseries.png     # 示例图表
├── tests/                 # 单元测试
├── requirements.txt       # Python依赖
├── LICENSE                # 许可证
└── README.md              # 项目说明