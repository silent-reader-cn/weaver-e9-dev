# 泛微OA 数据表: `modefieldauthorize`

- **中文名称**: 数据关联授权基本信息表
- **所属模块**: `表单建模`
- **数据库表名**: `modefieldauthorize`
- **主键**: `id`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表中的id |
| 3 | `formid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_bill表中的id |
| 4 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表中的id |
| 5 | `opttype` | 权限项 | `integer` | - | 是 | 否 | 否 | - | - | 作废<br>0：查看<br>2：编辑 |
| 6 | `layoutid` | 布局id | `integer` | - | 是 | 否 | 否 | - | - | 对应modehtmllayout表中的id |
| 7 | `layoutlevel` | 布局级别 | `integer` | - | 是 | 否 | 否 | - | - | 当设置布局的时候 才会有布局级别 ，布局级别越小 布局的优先级别最高 |
