# 泛微OA 数据表: `fnainvoicesubject`

- **所属模块**: `财务管理`
- **数据库表名**: `fnainvoicesubject`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `invoiceserviceyype` | 货物或应税服务类型 | `varchar2` | 1000 | 是 | - |
| 3 | `subjectid` | 科目id | `integer` | - | 是 | - |
| 4 | `lastmodifytime` | 最后修改时间 | `varchar2` | 160 | 是 | - |
| 5 | `checkdate` | 错误出现日期 | `varchar2` | 20 | 是 | - |
