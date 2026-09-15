# 泛微OA 数据表: `hrmsalaryitem`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalaryitem`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `itemname` | 薪酬项名称 | `varchar2` | 400 | 是 | 薪酬项名称 |
| 3 | `itemcode` | 薪酬项代码 | `varchar2` | 400 | 是 | 薪酬项代码 |
| 4 | `itemtype` | 类型 | `char` | 1 | 是 | 4 :计算   1: 工资  3:税收  9: 福利计算 |
| 5 | `personwelfarerate` | 福利个人费率 | `integer` | - | 是 | 福利个人费率 |
| 6 | `companywelfarerate` | 福利公司费率 | `integer` | - | 是 | 福利公司费率 |
| 7 | `taxrelateitem` | 税收基准项目 | `integer` | - | 是 | 税收基准项目 |
| 8 | `amountecp` | 计算公式 | `varchar2` | 1000 | 是 | 计算公式 |
| 9 | `feetype` | 费用类型 | `integer` | - | 是 | 费用类型 |
| 10 | `isshow` | 是否显示 | `char` | 1 | 是 | 是否显示 |
| 11 | `showorder` | 显示顺序 | `integer` | - | 是 | 显示顺序 |
| 12 | `ishistory` | 是否记录历史变动 | `char` | 1 | 是 | 是否记录历史变动 |
| 13 | `applyscope` | 应用范围 | `integer` | - | 是 | 应用范围 |
| 14 | `subcompanyid` | 分部id | `integer` | - | 是 | 分部id |
| 15 | `calmode` | 计算方式 | `integer` | - | 是 | 计算方式 |
| 16 | `directmodify` | 是否可以直接修改工资单 | `integer` | - | 是 | 是否可以直接修改工资单 |
| 17 | `companypercent` | 公司百分比 | `float` | 22 | 是 | 公司百分比 |
| 18 | `personalpercent` | 个人百分比 | `float` | 22 | 是 | 个人百分比 |
