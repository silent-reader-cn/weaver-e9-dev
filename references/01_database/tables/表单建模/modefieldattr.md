# 泛微OA 数据表: `modefieldattr`

- **中文名称**: 布局字段属性表
- **所属模块**: `表单建模`
- **数据库表名**: `modefieldattr`
- **主键**: `id`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表中的id |
| 3 | `formid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_bill中的id |
| 4 | `type` | 布局类型 | `integer` | - | 是 | 否 | 否 | - | - | 0、显示；<br>1、新建；<br>2、编辑；<br>3、监控；<br>4、打印 |
| 5 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表中的id |
| 6 | `attrcontent` | 字段属性内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 字段属性内容 |
| 7 | `caltype` | 计算类型 | `integer` | - | 是 | 否 | 否 | - | - | 1:dofieldsql<br>2:dofieldmath<br>3:dofielddate<br>4:dofieldsap |
| 8 | `othertype` | 日期计算排除工作日 | `integer` | - | 是 | 否 | 否 | - | - | 1：日期计算排除非工作日<br>0：日期计算不排除非工作日 |
| 9 | `transtype` | 转换类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：金额转换显示<br>2：千分位转换显示<br>0：取消 |
| 10 | `layoutid` | 布局id | `integer` | - | 是 | 否 | 否 | - | - | 对应modehtmllayout表中的id |
| 11 | `datasource` | 数据源 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
