# 泛微OA 数据表: `meetingRoomScreenField`

- **所属模块**: `会议管理`
- **数据库表名**: `meetingRoomScreenField`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | - | - |
| 2 | `columns` | 对应数据库名称 | `varchar2` | 100 | - | 对应meeting表数据库字段名称 |
| 3 | `otherColumns` | 其他名称 | `varchar2` | 100 | - | 对应meeting表数据库字段名称 |
| 4 | `fieldLabel` | 名称 | `varchar2` | 50 | - | - |
| 5 | `transMethod` | 转换方法 | `varchar2` | 200 | - | 根据columns和otherColumns进行转换 |
| 6 | `isUse` | 是否使用 | `integer` | - | - | 0:未启用 1:启用 |
