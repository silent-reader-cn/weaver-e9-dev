# 泛微OA 数据表: `mode_selectitempagedetail`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_selectitempagedetail`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `mainid` | 主表id | `integer` | - | 否 | - |
| 3 | `name` | 名称 | `varchar2` | 1000 | 是 | - |
| 4 | `disorder` | 排序 | `number` | (15,2) | 是 | - |
| 5 | `defaultvalue` | 默认值 | `varchar2` | 1000 | 是 | - |
| 6 | `pathcategory` | 存放目录 | `varchar2` | 1000 | 是 | - |
| 7 | `maincategory` | 主目录 | `varchar2` | 1000 | 是 | - |
| 8 | `isaccordtosubcom` | 与分部一致 | `integer` | - | 是 | - |
| 9 | `pid` | 父id | `integer` | - | 是 | - |
| 10 | `statelev` | 选择框的值 | `integer` | - | 是 | - |
| 11 | `cancel` | 是否取消 | `integer` | - | 是 | 0--否，1--是 |
| 12 | `uuid` | 32位id | `varchar2` | 800 | 是 | - |
| 13 | `name1` | 名称1 | `varchar2` | 1000 | 是 | - |
| 14 | `name2` | 名称2 | `varchar2` | 1000 | 是 | - |
