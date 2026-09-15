# 泛微OA 数据表: `fnainvoicecheckfaillog`

- **所属模块**: `财务管理`
- **数据库表名**: `fnainvoicecheckfaillog`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `checktime` | 错误出现时间 | `varchar2` | 160 | 是 | - |
| 3 | `checkdate` | 错误出现日期 | `varchar2` | 160 | 是 | - |
| 4 | `requestid` | 流程requestid | `integer` | - | 是 | - |
| 5 | `userid` | 用户ID | `integer` | - | 是 | - |
| 6 | `interfacetype` | 接口类型 | `varchar2` | 80 | 是 | - |
| 7 | `interfaceurl` | 接口地址 | `varchar2` | 1000 | 是 | - |
| 8 | `failmsg` | 失败信息 | `varchar2` | 1000 | 是 | - |
| 9 | `handlestatus` | 处理状态 | `integer` | - | 是 | 1.已处理,其他未处理 |
| 10 | `handletime` | 处理时间 | `varchar2` | 160 | 是 | - |
| 11 | `handleuser` | 处理人员ID | `integer` | - | 是 | - |
