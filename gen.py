import pandas as pd
import folium
from folium.plugins import HeatMap
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import folium
from folium.plugins import HeatMap

# 准备数据
data = {
    '城市': ['北京', '上海', '天津', '东京', '武汉', '南京', '苏州', '杭州', '长崎', '台北', '京都', '首尔', '大连', '宜昌', '香港', '大阪', '神户', '横滨', '营口', '厦门'],
    '经度': [116.4074, 121.4737, 117.2010, 139.6917, 114.3052, 118.7969, 120.5853, 120.1614, 129.8779, 121.5654, 135.7681, 126.9780, 121.2593, 111.2865, 114.1694, 135.5023, 135.1955, 139.6380, 122.2248, 118.0894],
    '纬度': [39.9042, 31.2304, 39.0842, 35.6762, 30.5928, 32.0603, 31.2990, 30.2735, 32.7486, 25.0320, 35.0078, 37.5665, 38.9140, 30.6919, 22.3193, 34.6937, 34.6901, 35.4437, 40.6670, 24.4798],
    '频率': [2330, 1996, 539, 343, 283, 254, 251, 228, 201, 145, 144, 152, 80, 77, 97, 108, 47, 36, 32, 5]
}
df = pd.DataFrame(data)

# 使用cartopy绘制东亚地图
def plot_east_asia_map():
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([100, 150, 15, 50], crs=ccrs.PlateCarree())  # 设置地图范围为东亚地区
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    plt.title('East Asia City Frequency Heatmap')
    plt.show()

# 使用folium生成交互式热力图
def generate_heatmap():
    # 创建地图对象，中心点设为东亚地区
    m = folium.Map(location=[35, 120], zoom_start=4)
    
    # 添加热力图层
    heat_data = [[row['纬度'], row['经度'], row['频率']] for index, row in df.iterrows()]
    HeatMap(heat_data, radius=30).add_to(m)
    
    # 保存为HTML文件
    m.save('east_asia_heatmap.html')
    print("热力图已生成并保存为 'east_asia_heatmap.html'")

# 执行函数
plot_east_asia_map()
generate_heatmap()