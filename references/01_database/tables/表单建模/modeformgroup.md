# 泛微OA 数据表: `modeformgroup`

- **中文名称**: 布局明细组属性表
- **所属模块**: `表单建模`
- **数据库表名**: `modeformgroup`
- **主键**: `id`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表的id |
| 2 | `formid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表的id |
| 3 | `type` | 布局类型 | `integer` | - | 是 | 否 | 否 | - | - | 0、显示<br>1、新建<br>2、编辑<br>3、监控<br>4、打印 |
| 4 | `groupid` | 组id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `isadd` | 是否允许新增明细 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 6 | `isedit` | 是否允许修改已有明细 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 7 | `isdelete` | 是否允许删除已有明细 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 8 | `ishidenull` | 是否打印空明细 | `integer` | - | 是 | 否 | 否 | - | - | (暂保留) |
| 9 | `isneed` | 必须新增明细 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 10 | `isdefault` | 是否新增默认空明细 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 11 | `layoutid` | 布局id | `integer` | - | 是 | 否 | 否 | - | - | 对应modehtmllayout表的id |
| 12 | `iscopy` | 是否允许复制明细 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 13 | `isprintserial` | 是否允许打印 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 14 | `allowscroll` | 滚动条 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 15 | `isopensapmul` | 是否支持sap | `integer` | - | 是 | 否 | 否 | - | - | - |
