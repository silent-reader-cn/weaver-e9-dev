# 泛微OA 数据表: `QQMailLog`

- **所属模块**: `集成模块`
- **数据库表名**: `QQMailLog`
- **文档收录字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识 | `integer` | - | - | - |
| 2 | `LogDate` | 日志发生日期 | `varchar2` | 100 | - | - |
| 3 | `LogTime` | 日志发生时间 | `varchar2` | 100 | - | - |
| 4 | `operateRemark` | 同步对象 | `varchar2` | 1000 | - | - |
| 5 | `datatype` | 对象类型 | `integer` | - | - | 1,分部;2,部门;3,岗位;4,人员; |
| 6 | `operateType` | 同步类型 | `integer` | - | - | 1,初始化;2,新增;3,修改;4,删除; |
| 7 | `operateResult` | 同步结果 | `integer` | - | - | 1,成功;0,失败; |
| 8 | `fail_summary` | 失败原因 | `varchar2` | 4000 | - | - |
