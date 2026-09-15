# 泛微OA 数据表: `workflow_nodefieldattr`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodefieldattr`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 3 | `formid` | 表单id | `integer` | - | 是 | - |
| 4 | `isbill` | 是否单据 | `integer` | - | 是 | 1、是，2 |
| 5 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 6 | `attrcontent` | 字段属性公式字符 | `varchar2` | 4000 | 是 | - |
| 7 | `caltype` | 公式类型 | `integer` | - | 是 | 1、sql取值，2、数字字段计算，3、日期计算 |
| 8 | `othertype` | 其他属性 | `integer` | - | 是 | 日期字段计算排除非工作日 |
| 9 | `transtype` | 字段显示转换的方法标识 | `integer` | - | 是 | - |
| 10 | `datasourceid` | 外部数据源 | `varchar2` | 1000 | 是 | - |
