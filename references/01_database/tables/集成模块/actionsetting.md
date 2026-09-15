# 泛微OA 数据表: `actionsetting`

- **所属模块**: `集成模块`
- **数据库表名**: `actionsetting`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 无 |
| 2 | `actionname` | 接口动作名称 | `varchar2` | 1000 | 是 | 无 |
| 3 | `actionclass` | 接口动作类文件 | `varchar2` | 2000 | 是 | 无 |
| 4 | `typename` | 接口类型名称 | `varchar2` | 160 | 是 | 无 |
| 5 | `actionshowname` | 接口动作显示名称 | `varchar2` | 1000 | 是 | 无 |
| 6 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 无 |
| 7 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 无 |
| 8 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 无 |
| 9 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 无 |
| 10 | `javacode` | java代码 | `clob` | 4000 | 是 | 无 |
