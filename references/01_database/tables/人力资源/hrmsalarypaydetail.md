# 泛微OA 数据表: `hrmsalarypaydetail`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalarypaydetail`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `payid` | 工资月份id | `integer` | - | 是 | 工资月份id |
| 2 | `itemid` | 薪酬id | `varchar2` | 6 | 是 | 薪酬id |
| 3 | `hrmid` | 人力资源 | `integer` | - | 是 | 人力资源 |
| 4 | `salary` | 工资项金额 | `number` | (12,2) | 是 | 工资项金额 |
| 5 | `condition` | 换算后的条件 | `varchar2` | 1000 | 是 | 换算后的条件 |
| 6 | `formular` | 换算后的公式 | `varchar2` | 1000 | 是 | 换算后的公式 |
| 7 | `conditiondsp` | 条件页面显示 | `varchar2` | 1000 | 是 | 条件页面显示 |
| 8 | `formulardsp` | 公式页面显示 | `varchar2` | 1000 | 是 | 公式页面显示 |
| 9 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 10 | `status` | 关闭状态 | `integer` | - | 是 | 1：关闭，0：打开 |
| 11 | `sent` | 发送状态 | `integer` | - | 是 | 1：发送，0：未发送 |
