# 泛微OA 数据表: `apphomepagefolder`

- **所属模块**: `移动引擎`
- **数据库表名**: `apphomepagefolder`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `foldername` | 文件夹名称 | `varchar2` | 1000 | 是 | 文件夹名称 |
| 3 | `orderid` | 显示排序 | `integer` | - | 是 | 显示排序 |
| 4 | `pid` | 父级ID | `integer` | - | 是 | 父级ID |
| 5 | `appid` | 应用ID | `integer` | - | 是 | 应用ID |
