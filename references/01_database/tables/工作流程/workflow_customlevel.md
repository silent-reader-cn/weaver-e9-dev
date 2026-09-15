# 泛微OA 数据表: `workflow_customlevel`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_customlevel`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `number` | 10 | 否 | - |
| 2 | `defaultname` | 默认名称 | `varchar2` | 10 | 否 | 系统默认名称 |
| 3 | `customname` | 自定义名称 | `varchar2` | 100 | 否 | 用户自定义紧急程度名称 |
| 4 | `isfc` | 是否封存 | `varchar2` | 1 | 否 | 0未封存、1封存 |
| 5 | `showorder` | 紧急程度排序 | `number` | 10 | 否 | 紧急程度排序字段 |
| 6 | `applicationwfid` | 应用的流程id | `clob` | - | 否 | 暂未使用 |
