# 泛微OA 数据表: `mobileappmodelinfo`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobileappmodelinfo`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `appid` | 所属应用id | `integer` | - | 是 | 所属应用，mobileappbaseinfo表的id列外键 |
| 3 | `formid` | 表单id | `integer` | - | 是 | 模块对应的表单id，workflow_bill表的id列外键 |
| 4 | `isdelete` | 是否删除 | `integer` | - | 是 | 是否删除，1是，0否 |
| 5 | `entityname` | 模块名称 | `varchar2` | 1000 | 是 | 模块的中文名称(添加模块时从modeinfo表中取得的modename列) |
| 6 | `modelid` | 模块id | `integer` | - | 是 | 表单建模中模块的id(即和modeinfo表的id列对应) |
| 7 | `showorder` | 显示顺序 | `integer` | - | 是 | 显示顺序，升序排序，越小的值排序越靠前 |
