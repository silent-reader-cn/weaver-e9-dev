# 泛微OA 数据表: `hrmrewardsrecord`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmrewardsrecord`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `rewardsdate` | 奖惩时间 | `char` | 10 | 是 | 奖惩时间 |
| 4 | `rewardstype` | 奖惩类型 | `integer` | - | 是 | 奖惩类型 |
| 5 | `remark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 6 | `createid` | 创建人id | `integer` | - | 是 | 创建人id |
| 7 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 8 | `createtime` | 创建时间 | `char` | 8 | 是 | 创建时间 |
| 9 | `lastmoderid` | 最后修改人id | `integer` | - | 是 | 最后修改人id |
| 10 | `lastmoddate` | 最后修改日期 | `char` | 10 | 是 | 最后修改日期 |
| 11 | `lastmodtime` | 最后修改时间 | `char` | 8 | 是 | 最后修改时间 |
