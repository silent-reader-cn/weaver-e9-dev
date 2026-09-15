# 泛微OA 数据表: `mobileappbaseinfo`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobileappbaseinfo`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `subcompanyid` | 分部ID | `varchar2` | 11 | 是 | 分部ID |
| 2 | `createdate` | 创建日期 | `varchar2` | 160 | 是 | 创建日期 |
| 3 | `modifydate` | 修改日期 | `varchar2` | 160 | 是 | 修改日期 |
| 4 | `creator` | 创建人ID | `integer` | 11 | 是 | 创建人ID |
| 5 | `category` | 类型 | `integer` | 11 | 是 | 类型 |
| 6 | `id` | 主键 | `integer` | - | 否 | - |
| 7 | `appname` | 应用名称 | `varchar2` | 1000 | 是 | 应用的名称 |
| 8 | `picpath` | 图标路径 | `varchar2` | 1024 | 是 | 应用对应的图标路径，如/mobilemode/images/a.png |
| 9 | `descriptions` | 描述 | `varchar2` | 1000 | 是 | 应用的描述信息 |
| 10 | `showorder` | 显示顺序 | `integer` | - | 是 | 显示顺序，升序排序，越小的值排序越靠前 |
| 11 | `isdelete` | 是否删除 | `integer` | - | 是 | 是否删除，1是，0否 |
| 12 | `formid` | 表单id | `integer` | - | 是 | 无用，已废弃 |
| 13 | `ispublish` | 是否发布 | `integer` | - | 是 | 应用发布状态：1发布，2下架 |
| 14 | `modelid` | 模块id | `integer` | - | 是 | 无用，已废弃 |
| 15 | `publishid` | 发布id | `varchar2` | 1000 | 是 | 发布到emobile配置文件中对应component的id |
| 16 | `hasheader` | 应用是否包含头部 | `varchar2` | 10 | 是 | 为1时包含头部，为空或者0则不包含头部 |
| 17 | `skin` | 皮肤 | `varchar2` | 500 | 是 | 存放该应用所引用的皮肤id，该id为32位的uuid |
