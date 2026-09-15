# 泛微OA 数据表: `fnacontrolschemedtl`

- **所属模块**: `财务管理`
- **数据库表名**: `fnacontrolschemedtl`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `mainid` | 预算方案id | `integer` | - | 是 | fnafeewfinfo表pk |
| 3 | `kmidscondition` | 预算科目 | `integer` | - | 是 | 1：属于； 2：不属于； |
| 4 | `kmids` | 科目id | `varchar2` | 4000 | 是 | 控制：科目id（多个） |
| 5 | `orgtype` | 费用单位类型 | `integer` | - | 是 | 1：分部； 2：部门； 3：个人； 18004：成本中心； |
| 6 | `orgidscondition` | 费用单位 | `integer` | - | 是 | 1：属于； 2：不属于 |
| 7 | `orgids` | 费用单位id | `varchar2` | 4000 | 是 | 控制：费用单位（多个） |
| 8 | `intensity` | 费控强度 | `integer` | - | 是 | 1：不控制； 2：强控； 3：弱控； |
| 9 | `promptsc` | 校验提示：简体中文 | `varchar2` | 4000 | 是 | - |
| 10 | `prompttc` | 校验提示：繁体中文 | `varchar2` | 4000 | 是 | 0：预算提交校验； 1：借款、还款、冲销合计金额提交校验； |
| 11 | `prompten` | 校验提示：英文 | `varchar2` | 4000 | 是 | 1：是； 其他：不是； |
