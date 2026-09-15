# 泛微OA 数据表: `sms_interface`

- **所属模块**: `短信模块`
- **数据库表名**: `sms_interface`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | 0 | 否 | &nbsp; |
| 2 | `name` | 接口相关名称 | `varchar2` | 1000 | 是 | 接口描述 |
| 3 | `keyword` | 关键字 | `varchar2` | 1000 | 是 | &nbsp; |
| 4 | `type` | 接口类型 | `varchar2` | 800 | 是 | http webservice sdk |
| 5 | `remark` | 备注 | `varchar2` | 2000 | 是 | &nbsp; |
| 6 | `clazzname` | 实现接口全路径 | `varchar2` | 1000 | 是 | 接口类的全路径 |
| 7 | `interfacetype` | 类型 | `integer` | 0 | 是 | 0 系统 1自定义（预留） |
| 8 | `versinno` | 版本 | `number` | (6,2) | 是 | 当前类版本 |
| 9 | `dsporder` | 显示排序 | `number` | (6,2) | 是 | 选择页面排序 |
