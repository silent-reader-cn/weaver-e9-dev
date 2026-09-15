# 泛微OA 数据表: `hrmorggrouprelated`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmorggrouprelated`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `orggroupid` | 群组id | `integer` | - | 是 | 群组id |
| 3 | `type` | 关联类型 | `integer` | - | 是 | 1.人员、2. 分部、3.部门、4.角色、5.所有人 |
| 4 | `content` | 关联对象 | `integer` | - | 是 | 如果当关联的类型为角色的时候. 其值为角色id角色级别id(0: 表部门 1：表分部 2：表总部)格式如 230其中最后一位表示角色级别id |
| 5 | `seclevelfrom` | 安全级别最小值 | `integer` | - | 是 | 安全级别最小值 |
| 6 | `seclevelto` | 安全级别最大值 | `integer` | - | 是 | 安全级别最大值 |
| 7 | `relatedlevel` | 关联级别 | `varchar2` | 80 | 否 | 关联级别 |
| 8 | `subcompanyid` | 分部id | `varchar2` | 80 | 是 | 分部id   分部表：hrmsubcompany |
| 9 | `departmentid` | 部门id | `varchar2` | 80 | 是 | 部门id    部门表：hrmdepartment |
| 10 | `lowerlevel` | 低级别 | `varchar2` | 80 | 否 | 低级别 |
