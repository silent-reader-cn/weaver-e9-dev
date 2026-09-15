# 泛微OA 数据表: `fnafeewfinfofield`

- **所属模块**: `财务管理`
- **数据库表名**: `fnafeewfinfofield`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `iswffieldlinkage` | （作废） | `integer` | - | 是 | - |
| 2 | `controlflowsubmission` | 预申请流程是否：控制流程提交 | `integer` | - | 是 | 0:不控制；1：控制(默认选中) |
| 3 | `automatictake` | 报销流程中 是否在对应字段 【承担主体】 中带出带出 当前登录人员的 | `integer` | - | 是 | 报销流程中 是否在对应字段 【承担主体】 中带出带出 当前登录人员的 【人员/部门/分部/成本中心】 1：是； 其他：不是； |
| 4 | `controlborrowingwf` | 还款（报销）流程中 是否通过申请人来进行 可选借款流程过滤 | `integer` | - | 是 | 1：是； 其他：不是； |
| 5 | `id` | 主键 | `integer` | - | 否 | - |
| 6 | `mainid` | 主表主键 | `integer` | - | 是 | fnafeewfinfo表pk |
| 7 | `workflowid` | 流程workflowid | `integer` | - | 是 | - |
| 8 | `formid` | 流程表单id | `integer` | - | 是 | - |
| 9 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 10 | `isdtl` | 是否是明细表字段 | `integer` | - | 是 | 1：是； 0：否； |
| 11 | `showalltype` | 显示所有类型的字段 | `integer` | - | 是 | 是否在后台维护字段时，显示所有类型的字段；1：是； 0：否； |
| 12 | `dtlnumber` | 字段所属明细表序号 | `integer` | - | 是 | 0：主表； 其他：明细表序号； 第一张明细表序号为1； |
| 13 | `fieldvalue` | 流程表单字段的值 | `varchar2` | 4000 | 是 | - |
| 14 | `fieldvaltype` | 维度字段对应类型 | `integer` | - | 是 | - |
