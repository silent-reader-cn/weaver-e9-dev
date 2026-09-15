# 泛微OA 数据表: `workflow_groupdetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_groupdetail`
- **字段总数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `groupid` | 操作者组id | `integer` | - | 是 | - |
| 3 | `objid` | 相关对象id | `integer` | - | 是 | - |
| 4 | `level_n` | 相关级别 | `integer` | - | 是 | - |
| 5 | `level2_n` | 最大安全级别 | `integer` | - | 是 | - |
| 6 | `conditions` | 操作者条件 | `varchar2` | 4000 | 是 | - |
| 7 | `conditioncn0` | 条件串 | `varchar2` | 4000 | 是 | - |
| 8 | `signorder` | 会签关系 | `char` | 1 | 是 | 0:非会签，1：会签，2：依次逐个签 |
| 9 | `orders` | 操作者批次 | `number` | (5,2) | 是 | - |
| 10 | `iscoadjutant` | 是否抄送协办人 | `char` | 1 | 是 | 1：是 |
| 11 | `signtype` | 会签关系 | `char` | 1 | 是 | 0：非会签，1：会签，2：不影响流程流转 |
| 12 | `issyscoadjutant` | 系统设置协办人 | `char` | 1 | 是 | - |
| 13 | `issubmitdesc` | 是否可提交意见 | `char` | 1 | 是 | - |
| 14 | `ispending` | 未查看一直停留在待办 | `char` | 1 | 是 | - |
| 15 | `isforward` | 是否可转发 | `char` | 1 | 是 | - |
| 16 | `ismodify` | 是否可修改表单内容 | `char` | 1 | 是 | - |
| 17 | `coadjutants` | 抄送协办人条件 | `varchar2` | 1000 | 是 | - |
| 18 | `coadjutantcn` | 抄送协办人条件（中文） | `varchar2` | 1000 | 是 | - |
| 19 | `deptfield` | 部门字段 | `varchar2` | 1000 | 是 | - |
| 20 | `subcompanyfield` | 子公司字段 | `varchar2` | 1000 | 是 | - |
| 21 | `virtualid` | 组织维度id | `varchar2` | 80 | 是 | - |
| 22 | `rulerelationship` | 规则间关系 | `char` | 1 | 是 | - |
| 23 | `conditioncn` | 操作者条件（中文） | `clob` | 4000 | 是 | - |
| 24 | `bhxj` | 是否包含下级 | `integer` | - | 是 | - |
