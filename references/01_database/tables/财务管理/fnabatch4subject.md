# 泛微OA 数据表: `fnabatch4subject`

- **所属模块**: `财务管理`
- **数据库表名**: `fnabatch4subject`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `groupdispalyorder` | 分组显示排序 | `varchar2` | 1000 | 是 | - |
| 2 | `budgetaccount` | 预算金额 | `number` | (18,2) | 是 | - |
| 3 | `str4k` | 字符串 | `varchar2` | 4000 | 是 | - |
| 4 | `str4k01` | 字符串1 | `varchar2` | 4000 | 是 | - |
| 5 | `str4k02` | 字符串2 | `varchar2` | 4000 | 是 | - |
| 6 | `str4k03` | 字符串3 | `varchar2` | 4000 | 是 | - |
| 7 | `str4k04` | 字符串4 | `varchar2` | 4000 | 是 | - |
| 8 | `str4k05` | 字符串5 | `varchar2` | 4000 | 是 | - |
| 9 | `guid1` | uuid | `char` | 32 | 是 | - |
| 10 | `id` | 主键 | `integer` | - | 是 | - |
| 11 | `groupctrl` | 统一费控 | `char` | 1 | 是 | - |
| 12 | `iseditfeetypeguid` | 当前科目所属可编制预算科目的GUID标识 | `char` | 32 | 是 | - |
| 13 | `iseditfeetypeid` | 当前科目所属可编制预算科目的id | `integer` | - | 是 | - |
| 14 | `groupctrlguid` | 当前科目所属统一费控预算科目的GUID标识 | `char` | 32 | 是 | - |
| 15 | `archive` | 封存 | `integer` | - | 是 | - |
| 16 | `feeperiod` | 预算周期 | `integer` | - | 是 | - |
| 17 | `groupctrlid` | 当前科目所属统一费控预算科目的id | `integer` | - | 是 | - |
