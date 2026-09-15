# 泛微OA 数据表: `apphomepage`

- **所属模块**: `移动引擎`
- **数据库表名**: `apphomepage`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `color` | 颜色 | `varchar2` | 400 | 是 | 颜色 |
| 2 | `pid` | 分组ID | `integer` | - | 是 | 分组ID |
| 3 | `prew_img` | 预览图片 | `varchar2` | 1000 | 是 | 预览图片 |
| 4 | `version` | 版本 | `varchar2` | 400 | 是 | 版本 |
| 5 | `id` | 主键 | `integer` | - | 否 | - |
| 6 | `appid` | 应用id | `integer` | - | 是 | 所属应用，mobileappbaseinfo表的id列外键 |
| 7 | `formuiids` | 模块布局ID | `varchar2` | 1024 | 是 | 模块UI对应的ID |
| 8 | `pagecontent` | 页面内容 | `clob` | 4000 | 是 | 存放页面html内容 |
| 9 | `mobiledeviceid` | 设备类型id | `integer` | - | 是 | 设备类型，mobiledevice表id列外键 |
| 10 | `parentid` | 父id | `integer` | - | 是 | 父id，和本表id列自身关联 |
| 11 | `pagename` | 页面名称 | `varchar2` | 1000 | 是 | 自定义页面的中文名称 |
| 12 | `pagedesc` | 页面描述 | `varchar2` | 1000 | 是 | 自定义页面描述信息 |
| 13 | `ishomepage` | 是否首页 | `integer` | - | 是 | 是否是首页，1为是，0或者空为否 |
| 14 | `pageattr` | 页面属性 | `clob` | 4000 | 是 | 页面本身的一些属性设置，json数据格式 |
| 15 | `orderid` | 顺序 | `integer` | - | 是 | 显示顺序，升序排序，越小的值排序越靠前 |
