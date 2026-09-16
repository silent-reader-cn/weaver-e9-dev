# 泛微OA 数据表: `mode_selectitempagedetail`

- **中文名称**: 公共选择项明细表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_selectitempagedetail`
- **主键**: `id`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `mainid` | 主表id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `name` | 名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `disorder` | 排序 | `number` | (15,2) | 是 | 否 | 否 | - | - | - |
| 5 | `defaultvalue` | 默认值 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `pathcategory` | 存放目录 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `maincategory` | 主目录 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `isaccordtosubcom` | 与分部一致 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `pid` | 父id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `statelev` | 选择框的值 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `cancel` | 是否取消 | `integer` | - | 是 | 否 | 否 | - | - | 0--否，1--是 |
| 12 | `uuid` | 32位id | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 13 | `name1` | 名称1 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 14 | `name2` | 名称2 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
