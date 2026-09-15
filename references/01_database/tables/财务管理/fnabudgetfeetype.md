# 泛微OA 数据表: `fnabudgetfeetype`

- **所属模块**: `财务管理`
- **数据库表名**: `fnabudgetfeetype`
- **字段总数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `groupctrlguid` | 当前科目所属统一费控预算科目的GUID标识 | `char` | 32 | 是 | 当前科目所属统一费控预算科目的GUID标识 |
| 2 | `displayorder` | 显示顺序 | `number` | (6,3) | 是 | - |
| 3 | `groupctrlid` | 当前科目所属统一费控预算科目的id | `integer` | - | 是 | 当前科目所属统一费控预算科目的id |
| 4 | `iseditfeetypeguid` | 当前科目所属可编制预算科目的GUID标识 | `char` | 32 | 是 | 作废 |
| 5 | `iseditfeetypeid` | 当前科目所属可编制预算科目的id | `integer` | - | 是 | 当前科目所属可编制预算科目的id |
| 6 | `allsupsubjectids` | 所有父级科目id | `varchar2` | 900 | 是 | 当前科目的所有上级科目id的集合，从左至右按科目层级从上至下依次排列，各个科目id之间使用英文半角逗号分隔 |
| 7 | `budgetcanbenegative` | 预算可为负数 | `integer` | - | 是 | 1:预算可为负数；其他不可为负数 |
| 8 | `groupdispalyorder` | 科目分组排序字段 | `varchar2` | 1000 | 是 | 可直接order by该字段，获得顺序即和科目树的展现顺序完全一致 |
| 9 | `codename2` | 科目会计编码 | `varchar2` | 800 | 是 | - |
| 10 | `id` | 主键 | `integer` | - | 否 | - |
| 11 | `name` | 名称 | `varchar2` | 600 | 是 | - |
| 12 | `description` | 描述 | `varchar2` | 1000 | 是 | - |
| 13 | `feeperiod` | 预算周期 | `integer` | - | 是 | 1：月度；2：季度；3：半年度；4：年度； |
| 14 | `feetype` | 科目种类 | `integer` | - | 是 | 1：支出； 2：收入 |
| 15 | `agreegap` | 允许偏差 | `integer` | - | 是 | 百分比 |
| 16 | `feelevel` | 科目级别 | `integer` | - | 是 | 1： 一级科目；2： 二级；3： 三级；......... |
| 17 | `supsubject` | 父级科目id | `integer` | - | 是 | - |
| 18 | `alertvalue` | 预警值 | `integer` | - | 是 | 百分比 |
| 19 | `archive` | 封存 | `integer` | - | 是 | 0、null：未封存；1：封存； |
| 20 | `feectllevel` | 作废 | `integer` | - | 是 | 作废 |
| 21 | `groupctrl` | 统一费控 | `char` | 1 | 是 | 预算控制时汇总下级科目费用进行统一控制 |
| 22 | `iseditfeetype` | 是否是可编制预算科目 | `integer` | - | 是 | 1：可编制；其他不可编制； |
| 23 | `codename` | 科目编码 | `varchar2` | 800 | 是 | - |
| 24 | `budgetautomove` | 是否结转 | `integer` | - | 是 | 1：结转；其他不结转；当前科目是否进行结转 |
