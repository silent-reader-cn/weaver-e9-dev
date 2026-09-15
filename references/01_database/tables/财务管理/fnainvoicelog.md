# 泛微OA 数据表: `fnainvoicelog`

- **所属模块**: `财务管理`
- **数据库表名**: `fnainvoicelog`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `msg` | 错误信息 | `varchar2` | 1000 | 是 | - |
| 2 | `ocrtype` | 接口类型 | `varchar2` | 80 | 是 | OCR:影像识别;token：获取token;openid：获取openid;verify：验票 |
| 3 | `id` | 主键 | `integer` | - | 否 | - |
| 4 | `interfacetype` | 调用接口类型 | `varchar2` | 80 | 是 | - |
| 5 | `posttime` | 接口调用时间 | `varchar2` | 160 | 是 | YYYY-MM-DD HH:MM:SS |
| 6 | `userid` | 用户ID | `integer` | - | 是 | - |
| 7 | `status` | 调用状态 | `varchar2` | 80 | 是 | 成功、失败 |
