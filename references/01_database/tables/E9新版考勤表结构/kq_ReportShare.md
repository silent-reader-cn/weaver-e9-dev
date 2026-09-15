# 泛微OA 数据表: `kq_ReportShare`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_ReportShare`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `ID` | 主键ID | `integer` | 11 | 否 | 主键 |
| 2 | `reportName` | 报表类型 | `integer` | 11 | 否 | 报表类型：1-考勤报表、2-月考勤日历报表、3-原始打卡记录报表、4-员工假期余额 |
| 3 | `resourceType` | 对象类型 | `integer` | 11 | 否 | 对象类型：1-人力资源、7-分权管理员、8-系统管理员 |
| 4 | `resourceId` | 对象 | `integer` | 11 | 否 | 对象 |
| 5 | `shareLevel` | 共享级别 | `integer` | 11 | 否 | 共享级别0-分部、1-部门、2-岗位、3-人力资源、4-所有人 |
| 6 | `subcomId` | 分部ID | `varchar2` | 200 | 否 | 分部ID |
| 7 | `deptId` | 部门ID | `varchar2` | 200 | 否 | 部门ID |
| 8 | `jobtitleId` | 岗位ID | `varchar2` | 200 | 否 | 岗位ID |
| 9 | `userId` | 人力资源ID | `varchar2` | 200 | 否 | 人力资源ID |
| 10 | `forAllUser` | 是否是所有人 | `integer` | 11 | 否 | 是否是所有人：0-否、1-是 |
