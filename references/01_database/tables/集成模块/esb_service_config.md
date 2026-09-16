# 泛微OA 数据表: `esb_service_config`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_service_config`
- **文档收录字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `type` | 接口类别 | `varchar2` | 100 | - | java.jms,amqp,http,jdbc,proc |
| 2 | `clazz` | 接口执行类 | `varchar2` | 800 | - | - |
| 3 | `titleLable` | 接口显示名多语言标记 | `varchar2` | 100 | - | - |
| 4 | `description` | 说明 | `varchar2` | 1000 | - | - |
