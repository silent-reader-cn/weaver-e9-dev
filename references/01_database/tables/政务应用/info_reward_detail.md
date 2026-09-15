# 泛微OA 数据表: `info_reward_detail`

- **所属模块**: `政务应用`
- **数据库表名**: `info_reward_detail`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `mainid` | 加分项id | `integer` | - | 是 | - |
| 4 | `type` | 类型 | `integer` | - | 是 | 0指定刊型  1指定栏目 |
| 5 | `j_type` | 刊型id | `integer` | - | 是 | - |
| 6 | `score` | 得分 | `float` | - | 是 | - |
| 7 | `j_column` | 栏目id | `integer` | - | 是 | - |
