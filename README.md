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

## 项目结构

- **`env-monitor-system/`** - 项目根目录
  - **`data/`** - 存放所有数据文件
    - `sensor_data.csv` - 主数据集，包含温度、湿度、PM2.5等传感器读数。
    - `generate_data.py` - 用于生成模拟数据的Python脚本。
  - **`src/`** - 存放项目所有源代码
    - `data_loader.py` - 负责数据读取和预处理的模块。
    - `data_analysis.py` - 核心数据分析与统计模块。
    - `visualization.py` - 生成图表和可视化结果的模块。
    - `main.py` - 程序主入口，协调各模块工作。
  - **`docs/`** - 项目文档和分析报告
    - `report.md` - 数据分析报告模板（Markdown格式）。
    - `timeseries.png` - 由程序生成的示例时间序列图。
  - **`tests/`** - 存放单元测试脚本。
  - `requirements.txt` - 列出运行本项目所需的所有Python库。
  - `LICENSE` - 本项目采用的开源许可证（如MIT）。
  - `README.md` - 您正在阅读的项目总览文档。