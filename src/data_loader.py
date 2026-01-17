import pandas as pd
import os

class DataLoader:
    """数据加载器"""

    def __init__(self, data_path='data/sensor_data.csv'):
        self.data_path = data_path
        self.data = None

    def load_data(self):
        """加载CSV数据"""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"数据文件不存在: {self.data_path}")

        self.data = pd.read_csv(self.data_path, encoding='utf-8')
        self.data['date'] = pd.to_datetime(self.data['date'])
        return self.data

    def get_data(self):
        """获取数据"""
        if self.data is None:
            self.load_data()
        return self.data

    def get_summary(self):
        """获取数据摘要"""
        if self.data is None:
            self.load_data()
        return {
            'shape': self.data.shape,
            'columns': list(self.data.columns),
            'date_range': (self.data['date'].min(), self.data['date'].max()),
            'locations': self.data['location'].unique().tolist()
        }

# 测试代码
if __name__ == '__main__':
    loader = DataLoader()
    data = loader.load_data()
    print("数据加载成功！")
    print(data.head())
    print("\n数据摘要:")
    print(loader.get_summary())