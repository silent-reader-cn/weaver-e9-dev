# 泛微OA 数据表: `hrmperformanceappendrule`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformanceappendrule`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `rulename` | 规则名称 | `varchar2` | 800 | 是 | 规则名称 |
| 3 | `memo` | 规则定义 | `varchar2` | 1000 | 是 | 规则定义 |
| 4 | `conditions` | 条件 | `varchar2` | 1000 | 是 | 条件 |
| 5 | `conditionsum` | 条件数目 | `varchar2` | 1000 | 是 | 条件数目 |
| 6 | `formula` | 公式 | `varchar2` | 1000 | 是 | 公式 |
| 7 | `formulasum` | 公式数目 | `varchar2` | 1000 | 是 | 公式数目 |
| 8 | `status` | 状态 | `char` | 1 | 是 | 是否起用 0启用，1关闭 |
| 9 | `deptid` | 部门id | `varchar2` | 1000 | 是 | 部门id |
| 10 | `hrmid` | 人员id | `varchar2` | 1000 | 是 | 人员id |
| 11 | `postid` | 岗位id | `varchar2` | 1000 | 是 | 岗位id |
| 12 | `formuladeptid` | 公式关联部门id | `varchar2` | 1000 | 是 | 公式关联部门id |
| 13 | `formulahrmid` | 公式关联人员id | `varchar2` | 1000 | 是 | 公式关联人员id |
| 14 | `formulapostid` | 公式关联岗位id | `varchar2` | 1000 | 是 | 公式关联岗位id |
