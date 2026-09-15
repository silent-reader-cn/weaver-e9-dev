# 泛微OA 数据表: `hrmsalarycomponentdetail`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalarycomponentdetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `componentid` | 人力资源原有工资类型id | `integer` | - | 是 | 人力资源原有工资类型id |
| 2 | `detailmark` | 明细名称 | `varchar2` | 480 | 是 | 明细名称 |
| 3 | `joblevel` | 岗位级别 | `integer` | - | 是 | 岗位级别 |
| 4 | `salarysum` | 工资总金额 | `number` | (10,3) | 是 | 工资总金额 |
| 5 | `editable` | 是否可编辑 | `char` | 1 | 是 | 0是不可，1可编辑 |
