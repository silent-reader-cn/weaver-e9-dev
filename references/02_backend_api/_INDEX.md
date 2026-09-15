# 泛微 E9 后端接口总索引

> 共 **538** 个接口，按官网 8 大模块分类。大模块已切分为多个小文件，下表「文件」列指向具体文件。

> 索引由 `scripts/build_index.py` 自动生成，请勿手工编辑。
> 检索接口请用统一检索脚本：
> ```bash
> python scripts/search.py getToDoWorkflowRequestList
> python scripts/search.py 分部 --scope api --brief
> ```

## 协作管理

| 接口 | 方法 | 地址 | 文件 |
|---|---|---|---|
| 协作-协作交流-列表(layout 1为数图模式;2为列表模式) | GET | `/api/cowork/base/getCoworkList` | [协作管理.md](协作管理.md) |
| 协作后台版块设置-版块列表 | GET | `/api/cowork/type/getCoworkTypeList` | [协作管理.md](协作管理.md) |
| 协作后台类别设置-类别列表 | GET | `/api/cowork/maintype/getCoworkMainTypeList` | [协作管理.md](协作管理.md) |

## 邮件模块

| 接口 | 方法 | 地址 | 文件 |
|---|---|---|---|
| 获取邮件总数、未读数 | GET | `/api/email/base/refreshCount` | [邮件模块.md](邮件模块.md) |
| 邮件列表 | GET | `/api/email/list/allList` | [邮件模块.md](邮件模块.md) |
| 邮件监控 监控日志列表 | GET | `/api/email/monitor/monitorLogList` | [邮件模块.md](邮件模块.md) |

## 表单建模

| 接口 | 方法 | 地址 | 文件 |
|---|---|---|---|
| 保存快捷搜索信息 | POST | `/api/cube/list/saveQuickSearchInfo` | [表单建模.md](表单建模.md) |
| 保存查询模板默认值 | GET | `/api/cube/search/setDefault` | [表单建模.md](表单建模.md) |
| 初始化列宽接口 | GET | `/api/cube/search/cleanCol` | [表单建模.md](表单建模.md) |
| 删除数据接口 | GET | `/api/cube/expand/deleteData` | [表单建模.md](表单建模.md) |
| 判断数据是否改变接口 | POST | `/api/cube/search/checkDataChange` | [表单建模.md](表单建模.md) |
| 卡片数据保存接口(常用) | POST | `/api/cube/new/card/doSubmit` | [表单建模.md](表单建模.md) |
| 权限校验接口 | GET | `/api/cube/new/card/checkCardRight` | [表单建模.md](表单建模.md) |
| 查询快捷搜索信息获取接口 | GET | `/api/cube/list/getQuickSearchInfo` | [表单建模.md](表单建模.md) |
| 获取主表字段信息 | GET | `/api/cube/new/card/mainFields` | [表单建模.md](表单建模.md) |
| 获取二维码信息 | GET | `/api/cube/new/card/getQRCode` | [表单建模.md](表单建模.md) |
| 获取卡片iframe设置 | GET | `/api/cube/new/card/getIframe` | [表单建模.md](表单建模.md) |
| 获取卡片布局基本信息 | GET | `/api/cube/new/card/layoutBase` | [表单建模.md](表单建模.md) |
| 获取卡片明细表数据 | GET | `/api/cube/new/card/getDetailFields` | [表单建模.md](表单建模.md) |
| 获取卡片条形码信息 | GET | `/api/cube/new/card/getBarCode` | [表单建模.md](表单建模.md) |
| 获取字段联动信息 | GET | `/api/cube/new/card/getInputEntry` | [表单建模.md](表单建模.md) |
| 获取属性联动信息 | GET | `/api/cube/new/card/getFieldAttrLinkPage` | [表单建模.md](表单建模.md) |
| 获取查询列表基本信息 | GET | `/api/cube/search/init` | [表单建模.md](表单建模.md) |
| 获取查询权限信息 | GET | `/api/cube/list/getRightInfo` | [表单建模.md](表单建模.md) |
| 获取查询相关信息 | GET | `/api/cube/search/getList` | [表单建模.md](表单建模.md) |

## 人力资源

| 接口 | 方法 | 地址 | 文件 |
|---|---|---|---|
| E7扫码登录 | POST | `/api/hrm/login/qrcode/loginQRCode` | [人力资源_01.md](人力资源_01.md) |
| 二次验证密码--验证二次验证密码和登录密码是否一样 | POST | `/api/hrm/secondarypwd/checkNewSecondaryPwd` | [人力资源_01.md](人力资源_01.md) |
| 人力资源导入历史记录查询条件 | GET | `/api/hrm/importlog/getHistorySearchCondition` | [人力资源_01.md](人力资源_01.md) |
| 人力资源系统信息 | GET | `/api/hrm/systeminfo/getHrmSystemInfoForm` | [人力资源_01.md](人力资源_01.md) |
| 人员列表查询条件 | GET | `/api/hrm/organization/getResourceSearchCondition` | [人力资源_01.md](人力资源_01.md) |
| 人员卡片小头像设置--保存头像 | POST | `/api/hrm/usericon/saveUserIcon` | [人力资源_01.md](人力资源_01.md) |
| 人员卡片工作历程 | GET | `/api/hrm/resource/total/getHrmResourceTotal` | [人力资源_01.md](人力资源_01.md) |
| 人员卡片栏目信息（流程、文档等） | GET | `/api/hrm/resource/getHrmResourceItem` | [人力资源_01.md](人力资源_01.md) |
| 人员卡片自定义字段 | GET | `/api/hrm/resourcefielddefined/getFieldDefinedInfo` | [人力资源_01.md](人力资源_01.md) |
| 人员卡片页签 | GET | `/api/hrm/resource/getHrmResourceTab` | [人力资源_01.md](人力资源_01.md) |
| 人员导入历史日志 | GET | `/api/hrm/importlog/getImportHistory` | [人力资源_01.md](人力资源_01.md) |
| 人员导入明细日志 | GET | `/api/hrm/importlog/getImportResult` | [人力资源_01.md](人力资源_01.md) |
| 人员导入表单 | GET | `/api/hrm/import/resource/getImportForm` | [人力资源_01.md](人力资源_01.md) |
| 人员导入进度列表 | GET | `/api/hrm/importlog/getImportProcessLog` | [人力资源_01.md](人力资源_01.md) |
| 人员小卡片信息 | GET | `/api/hrm/simpleinfo/getHrmSimpleInfo` | [人力资源_01.md](人力资源_01.md) |
| 人员登录失败日志列表 | GET | `/api/hrm/loginfailedlog/getSearchList` | [人力资源_01.md](人力资源_01.md) |
| 人员登录失败日志查询条件 | GET | `/api/hrm/loginfailedlog/getSearchCondition` | [人力资源_01.md](人力资源_01.md) |
| 人员登录接口 | POST | `/api/hrm/login/checkLogin` | [人力资源_01.md](人力资源_01.md) |
| 人员登录日志右键菜单 | GET | `/api/hrm/loginlog/getRightMenu` | [人力资源_01.md](人力资源_01.md) |
| 人员登录日志权限判断 | GET | `/api/hrm/loginlog/getHasRight` | [人力资源_01.md](人力资源_01.md) |
| 人员登录日志查询列表 | GET | `/api/hrm/loginlog/getSearchList` | [人力资源_01.md](人力资源_01.md) |
| 人员登录日志查询条件 | GET | `/api/hrm/loginlog/getAdvanceCondition` | [人力资源_01.md](人力资源_01.md) |
| 保存人员卡片自定义字段分组 | GET | `/api/hrm/resourcefielddefined/saveGroup` | [人力资源_01.md](人力资源_01.md) |
| 保存人员导入 | POST | `/api/hrm/import/resource/saveImport` | [人力资源_01.md](人力资源_01.md) |
| 保存分部自定义字段分组 | POST | `/api/hrm/subcompanyfielddefined/saveGroup` | [人力资源_01.md](人力资源_01.md) |
| 保存功能权限 | POST | `/api/hrm/rolefucrightset/saveRolesFucRightSet` | [人力资源_01.md](人力资源_01.md) |
| 保存加入常用组 | POST | `/api/hrm/organization/saveAddToGroup` | [人力资源_01.md](人力资源_01.md) |
| 保存机构权限 | POST | `/api/hrm/rolesstrrightset/saveRolesStrRightSet` | [人力资源_01.md](人力资源_01.md) |
| 保存权限明细 | POST | `/api/hrm/systemrightauthority/saveSystemRightAuthority` | [人力资源_01.md](人力资源_01.md) |
| 保存权限设置 | POST | `/api/hrm/systemrightgroup/saveSystemRightGroup` | [人力资源_01.md](人力资源_01.md) |
| 保存权限设置 | POST | `/api/hrm/systemrightgroup/addSystemRightRoles` | [人力资源_02.md](人力资源_02.md) |
| 保存组织设置接口 | POST | `/api/hrm/orgchart/saveorgchartset` | [人力资源_02.md](人力资源_02.md) |
| 保存部门自定义字段 | POST | `/api/hrm/departmentfielddefined/save` | [人力资源_02.md](人力资源_02.md) |
| 保存部门自定义字段分组 | POST | `/api/hrm/departmentfielddefined/saveGroup` | [人力资源_02.md](人力资源_02.md) |
| 分权管理--判断是否有权限 | GET | `/api/hrm/detachmanagerset/getHasRight` | [人力资源_02.md](人力资源_02.md) |
| 分权管理员--判断是否有权限 | GET | `/api/hrm/detachsysadmin/getHasRight` | [人力资源_02.md](人力资源_02.md) |
| 分级保护设置--判断是否具有权限 | GET | `/api/hrm/classifiedProtection/getHasRight` | [人力资源_02.md](人力资源_02.md) |
| 分部信息 | GET | `/api/hrm/organization/getSubCompanyFormFieldView` | [人力资源_02.md](人力资源_02.md) |
| 分部列表查询条件 | GET | `/api/hrm/organization/getSubCompanySearchCondition` | [人力资源_02.md](人力资源_02.md) |
| 分部浏览框-模糊搜索 | GET | `/api/public/browser/complete/164` | [人力资源_02.md](人力资源_02.md) |
| 分部浏览框-高级搜索 | GET | `/api/public/browser/data/164` | [人力资源_02.md](人力资源_02.md) |
| 分部自定义字段保存 | POST | `/api/hrm/subcompanyfielddefined/save` | [人力资源_02.md](人力资源_02.md) |
| 分部自定义字段删除 | POST | `/api/hrm/subcompanyfielddefined/del` | [人力资源_02.md](人力资源_02.md) |
| 分部自定义字段移动分组 | POST | `/api/hrm/subcompanyfielddefined/changegroup` | [人力资源_02.md](人力资源_02.md) |
| 分部自定义字段页签 | GET | `/api/hrm/subcompanyfielddefined/getTabInfo` | [人力资源_02.md](人力资源_02.md) |
| 删除分部 | POST | `/api/hrm/organization/delSubCompany` | [人力资源_02.md](人力资源_02.md) |
| 删除分部自定义字段分组 | POST | `/api/hrm/subcompanyfielddefined/delGroup` | [人力资源_02.md](人力资源_02.md) |
| 删除权限分组 | GET | `/api/hrm/systemrightgroup/delSystemRightGroup` | [人力资源_02.md](人力资源_02.md) |
| 删除权限明细 | POST | `/api/hrm/systemrightauthority/delSystemRightAuthority` | [人力资源_02.md](人力资源_02.md) |
| 删除权限角色引用 | POST | `/api/hrm/systemrightgroup/delSystemRightRoles` | [人力资源_02.md](人力资源_02.md) |
| 删除矩阵 | POST | `/api/hrm/matrix/pages/matrixList/delMatrixList` | [人力资源_02.md](人力资源_02.md) |
| 删除虚拟维度 | POST | `/api/hrm/organizationvirtual/delCompany` | [人力资源_02.md](人力资源_02.md) |
| 删除虚拟维度人员 | POST | `/api/hrm/organizationvirtual/delResource` | [人力资源_02.md](人力资源_02.md) |
| 删除虚拟维度分部 | POST | `/api/hrm/organizationvirtual/delSubCompany` | [人力资源_02.md](人力资源_02.md) |
| 删除虚拟维度部门 | POST | `/api/hrm/organizationvirtual/delDepartment` | [人力资源_02.md](人力资源_02.md) |
| 删除角色功能权限 | POST | `/api/hrm/rolefucrightset/delRolesFucRightSet` | [人力资源_02.md](人力资源_02.md) |
| 删除角色权限 | POST | `/api/hrm/rolesstrrightset/delRolesStrRightSet` | [人力资源_02.md](人力资源_02.md) |
| 删除部门 | POST | `/api/hrm/organization/delDepartment` | [人力资源_02.md](人力资源_02.md) |
| 删除部门自定义字段分组 | POST | `/api/hrm/departmentfielddefined/delGroup` | [人力资源_02.md](人力资源_02.md) |
| 单人力浏览框切换tab获取数据 | GET | `/api/public/browser/data/1` | [人力资源_02.md](人力资源_02.md) |
| 单人力浏览框模糊搜索 | POST | `/api/public/browser/complete/1` | [人力资源_03.md](人力资源_03.md) |
| 单人力浏览框高级搜索 | POST | `/api/public/browser/data/17` | [人力资源_03.md](人力资源_03.md) |
| 单人力浏览框高级搜索 | POST | `/api/public/browser/data/1` | [人力资源_03.md](人力资源_03.md) |
| 发送工资单 | POST | `/api/hrm/finance/salarymanage/sendSalaryManage` | [人力资源_03.md](人力资源_03.md) |
| 后端人力首页组织权限中心统计接口 | GET | `/api/hrm/common/getIndexInfo` | [人力资源_03.md](人力资源_03.md) |
| 在线人员分析--在线人员列表 | POST | `/api/hrm/online/getSearchResult` | [人力资源_03.md](人力资源_03.md) |
| 多人力浏览框切换tab获取数据 | GET | `/api/public/browser/data/17` | [人力资源_03.md](人力资源_03.md) |
| 多人力浏览框模糊搜索 | POST | `/api/public/browser/complete/17` | [人力资源_03.md](人力资源_03.md) |
| 导入日志列表 | GET | `/api/hrm/importlog/getImportColResultLog` | [人力资源_03.md](人力资源_03.md) |
| 封存分部 | POST | `/api/hrm/organization/doSubCompanyCancel` | [人力资源_03.md](人力资源_03.md) |
| 封存虚拟维度分部 | POST | `/api/hrm/organizationvirtual/doSubCompanyCancel` | [人力资源_03.md](人力资源_03.md) |
| 封存虚拟维度部门 | POST | `/api/hrm/organizationvirtual/doDepartmentCancel` | [人力资源_03.md](人力资源_03.md) |
| 封存部门 | POST | `/api/hrm/organization/doDepartmentCancel` | [人力资源_03.md](人力资源_03.md) |
| 岗位浏览框-模糊搜索 | GET | `/api/public/browser/complete/24` | [人力资源_03.md](人力资源_03.md) |
| 岗位浏览框-高级搜索 | GET | `/api/public/browser/data/24` | [人力资源_03.md](人力资源_03.md) |
| 工资单管理--关闭工资单 | POST | `/api/hrm/finance/salarymanage/closeSalaryManage` | [人力资源_03.md](人力资源_03.md) |
| 工资单管理--判断是否有权限 | GET | `/api/hrm/finance/salarymanage/getHasRight` | [人力资源_03.md](人力资源_03.md) |
| 工资单管理--生成工资单 | POST | `/api/hrm/finance/salarymanage/createSalaryManage` | [人力资源_03.md](人力资源_03.md) |
| 工资单管理--获取工资单管理查看表单 | POST | `/api/hrm/finance/salarymanage/getSalaryManageViewForm` | [人力资源_03.md](人力资源_03.md) |
| 工资单管理--获取工资单管理编辑表单 | POST | `/api/hrm/finance/salarymanage/getSalaryManageEditForm` | [人力资源_03.md](人力资源_03.md) |
| 批量编辑界面，保存批量调整部门所属分部表单 | POST | `/api/hrm/batchMaintenanceAdjustEdit/saveBatchSubcomid` | [人力资源_03.md](人力资源_03.md) |
| 批量编辑界面，获取批量调整上级部门表单 | POST | `/api/hrm/batchMaintenanceAdjustEdit/getBatchSupdepid` | [人力资源_03.md](人力资源_03.md) |
| 批量编辑界面，获取批量调整分部表单 | POST | `/api/hrm/batchMaintenanceAdjustEdit/getBatchSubcomid` | [人力资源_03.md](人力资源_03.md) |
| 批量编辑页面，保存批量分部上级信息 | POST | `/api/hrm/batchMaintenanceAdjustEdit/saveBatchSupSubcomid` | [人力资源_03.md](人力资源_03.md) |
| 批量编辑页面，保存批量调整上级部门表单 | POST | `/api/hrm/batchMaintenanceAdjustEdit/saveBatchSupdepid` | [人力资源_03.md](人力资源_03.md) |
| 批量调整保存部门信息 | POST | `/api/hrm/batchMaintenanceAdjust/saveBatchDepartment` | [人力资源_03.md](人力资源_03.md) |
| 批量调整分部信息 | POST | `/api/hrm/batchMaintenanceAdjust/batchSubcompany` | [人力资源_03.md](人力资源_03.md) |
| 批量调整界面，保存分部数据 | POST | `/api/hrm/batchMaintenanceAdjust/saveBatchSubcompany` | [人力资源_03.md](人力资源_03.md) |
| 批量调整页面，批量部门界面 | POST | `/api/hrm/batchMaintenanceAdjust/batchDepartment` | [人力资源_03.md](人力资源_03.md) |
| 批量重置密码 | POST | `/api/hrm/organization/saveBatchDefaultPwd` | [人力资源_03.md](人力资源_03.md) |
| 新增人虚拟维度员 | POST | `/api/hrm/organizationvirtual/addResourceToVirtual` | [人力资源_04.md](人力资源_04.md) |
| 新增分部 | POST | `/api/hrm/organization/addSubCompany` | [人力资源_04.md](人力资源_04.md) |
| 新增虚拟维度 | POST | `/api/hrm/organizationvirtual/addCompany` | [人力资源_04.md](人力资源_04.md) |
| 新增虚拟维度分部 | POST | `/api/hrm/organizationvirtual/addSubCompany` | [人力资源_04.md](人力资源_04.md) |
| 新增虚拟维度部门 | POST | `/api/hrm/organizationvirtual/addDepartment` | [人力资源_04.md](人力资源_04.md) |
| 新增部门 | POST | `/api/hrm/organization/addDepartment` | [人力资源_04.md](人力资源_04.md) |
| 机构权限列表 | POST | `/api/hrm/rolesstrrightset/getRolesStrRightSetList` | [人力资源_04.md](人力资源_04.md) |
| 机构权限表单 | GET | `/api/hrm/rolesstrrightset/getRolesStrRightSetForm` | [人力资源_04.md](人力资源_04.md) |
| 权限明细列表 | POST | `/api/hrm/systemrightauthority/getSystemRightAuthorityList` | [人力资源_04.md](人力资源_04.md) |
| 权限明细查询条件 | GET | `/api/hrm/systemrightauthority/getSystemRightAuthorityCondition` | [人力资源_04.md](人力资源_04.md) |
| 权限组Tab | GET | `/api/hrm/systemrightgroup/getSystemRightGroupTabInfo` | [人力资源_04.md](人力资源_04.md) |
| 权限组列表 | POST | `/api/hrm/systemrightgroup/getSystemRightGroupList` | [人力资源_04.md](人力资源_04.md) |
| 权限组查询条件 | GET | `/api/hrm/systemrightgroup/getSystemRightGroupCondition` | [人力资源_04.md](人力资源_04.md) |
| 权限组表单 | GET | `/api/hrm/systemrightgroup/getSystemRightGroupForm` | [人力资源_04.md](人力资源_04.md) |
| 权限角色引用查询列表 | POST | `/api/hrm/systemrightgroup/getSystemRightRolesList` | [人力资源_04.md](人力资源_04.md) |
| 权限角色引用查询条件 | GET | `/api/hrm/systemrightgroup/getSystemRightRolesCondition` | [人力资源_04.md](人力资源_04.md) |
| 权限调整--权限删除选择框列表 | GET | `/api/hrm/permissiontoadjustbrowser/list/D{key}` | [人力资源_04.md](人力资源_04.md) |
| 权限调整-权限删除选择框列表 | GET | `/api/hrm/permissiontoadjustbrowser/list/T{key}` | [人力资源_04.md](人力资源_04.md) |
| 权限调整-权限删除选择框条件 | GET | `/api/hrm/permissiontoadjustbrowser/condition/D{key}` | [人力资源_04.md](人力资源_04.md) |
| 权限调整-权限复制浏览框列表 | GET | `/api/hrm/permissiontoadjustbrowser/list/C{key}` | [人力资源_04.md](人力资源_04.md) |
| 权限调整-权限复制选择框条件 | GET | `/api/hrm/permissiontoadjustbrowser/condition/C{key}` | [人力资源_04.md](人力资源_04.md) |
| 权限调整-权限调整选择框条件 | GET | `/api/hrm/permissiontoadjustbrowser/condition/T{key}` | [人力资源_04.md](人力资源_04.md) |
| 权限调整列表 | POST | `/api/hrm/permissionsearch/getPermissionSearchResult` | [人力资源_04.md](人力资源_04.md) |
| 权限调整列表 | POST | `/api/hrm/permissiontoadjust/getPermissionToAdjustList` | [人力资源_04.md](人力资源_04.md) |
| 权限调整日志 | GET | `/api/hrm/permissiontoadjust/getProcessLog` | [人力资源_04.md](人力资源_04.md) |
| 权限调整检查对象是否有为完成的任务 | GET | `/api/hrm/permissiontoadjust/checkFromId` | [人力资源_04.md](人力资源_04.md) |
| 权限调整表单 | GET | `/api/hrm/permissiontoadjust/getPermissionToAdjustForm` | [人力资源_04.md](人力资源_04.md) |
| 权限查询表单 | GET | `/api/hrm/permissionsearch/getPermissionSearchForm` | [人力资源_04.md](人力资源_04.md) |
| 权限调整返回结果数据 | POST | `/api/hrm/permissiontoadjust/processData` | [人力资源_04.md](人力资源_04.md) |
| 查看部门信息 | GET | `/api/hrm/organization/getDepartmentFormFieldView` | [人力资源_04.md](人力资源_04.md) |
| 根据条件再次获取组织图表数据 | POST | `/api/hrm/orgchart/getOrgChartDataAjax` | [人力资源_05.md](人力资源_05.md) |
| 根据部门获取分部信息 | POST | `/api/hrm/batchmaintenanceadjust/getsubcompanyinfo` | [人力资源_05.md](人力资源_05.md) |
| 添加人员到虚拟维度 | POST | `/api/hrm/organization/saveResourceVirtualDepartmentSet` | [人力资源_05.md](人力资源_05.md) |
| 清除当前矩阵的离职人员 | POST | `/api/hrm/matrix/pages/matrixList/clearDimission` | [人力资源_05.md](人力资源_05.md) |
| 登录失败日志右键菜单 | GET | `/api/hrm/loginfailedlog/getRightMenu` | [人力资源_05.md](人力资源_05.md) |
| 登录失败日志权限判断 | GET | `/api/hrm/loginfailedlog/getHasRight` | [人力资源_05.md](人力资源_05.md) |
| 登录提醒 | POST | `/api/hrm/login/remindLogin` | [人力资源_05.md](人力资源_05.md) |
| 矩阵信息导出 | POST | `/api/hrm/matrix/pages/matrixList/matrixExport` | [人力资源_05.md](人力资源_05.md) |
| 矩阵新增保存 | POST | `/api/hrm/matrix/pages/matrixList/addMatrixList` | [人力资源_05.md](人力资源_05.md) |
| 管理分权权限判断 | GET | `/api/hrm/modulemanagerdetach/getHasRight` | [人力资源_05.md](人力资源_05.md) |
| 组织字段显示层级设置--获取右键菜单 | GET | `/api/hrm/organizationShowSet/getRightMenu` | [人力资源_05.md](人力资源_05.md) |
| 组织字段显示设置--保存 | POST | `/api/hrm/organizationShowSet/saveOrganizationShowSet` | [人力资源_05.md](人力资源_05.md) |
| 组织字段显示设置权限判断 | GET | `/api/hrm/organizationShowSet/getHasRight` | [人力资源_05.md](人力资源_05.md) |
| 组织显示设置--获取表单 | GET | `/api/hrm/organizationShowSet/getOrganizationShowSetForm` | [人力资源_05.md](人力资源_05.md) |
| 组织结构右键菜单 | POST | `/api/hrm/organization/getRightMenu` | [人力资源_05.md](人力资源_05.md) |
| 组织结构维护获取部门表单 | GET | `/api/hrm/organizationvirtual/getDepartmentFormField` | [人力资源_05.md](人力资源_05.md) |
| 组织结构页签 | POST | `/api/hrm/organization/getTabs` | [人力资源_05.md](人力资源_05.md) |
| 编辑分部信息 | POST | `/api/hrm/organization/editSubCompany` | [人力资源_05.md](人力资源_05.md) |
| 编辑工资单 | POST | `/api/hrm/finance/salarymanage/editsalarymanage` | [人力资源_05.md](人力资源_05.md) |
| 编辑总部 | POST | `/api/hrm/organization/editCompany` | [人力资源_05.md](人力资源_05.md) |
| 编辑权限角色引用 | GET | `/api/hrm/systemrightgroup/editsystemrightroles` | [人力资源_05.md](人力资源_05.md) |
| 编辑虚拟维度 | POST | `/api/hrm/organizationvirtual/editCompany` | [人力资源_05.md](人力资源_05.md) |
| 编辑虚拟维度分部 | POST | `/api/hrm/organizationvirtual/editSubCompany` | [人力资源_05.md](人力资源_05.md) |
| 编辑虚拟维度部门 | POST | `/api/hrm/organizationvirtual/editDepartment` | [人力资源_05.md](人力资源_05.md) |
| 编辑部门信息 | POST | `/api/hrm/organization/editDepartment` | [人力资源_05.md](人力资源_05.md) |
| 职务和岗位设置--职务列表 | GET | `/api/hrm/job/getJobActivityList` | [人力资源_05.md](人力资源_05.md) |
| 职务岗位设置--删除岗位 | POST | `/api/hrm/job/deleteJobTitle` | [人力资源_05.md](人力资源_05.md) |
| 职务岗位设置--删除职务 | POST | `/api/hrm/job/deleteJobActivity` | [人力资源_05.md](人力资源_05.md) |
| 职务岗位设置--判断是否有权限 | GET | `/api/hrm/job/getHasRight` | [人力资源_05.md](人力资源_05.md) |
| 职务岗位设置--岗位封存或解封 | POST | `/api/hrm/job/doCanceled` | [人力资源_05.md](人力资源_05.md) |
| 职务岗位设置--新增岗位 | POST | `/api/hrm/job/addJobTitle` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--新建职务 | POST | `/api/hrm/job/addJobActivity` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--添加职务类别 | POST | `/api/hrm/job/addJobGroup` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--编辑岗位 | POST | `/api/hrm/job/editeJobTitle` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--编辑职务 | POST | `/api/hrm/job/editeJobActivity` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--编辑职务类别 | POST | `/api/hrm/job/editeJobGroup` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--获取基本信息 | GET | `/api/hrm/job/getJobDetail` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--获取岗位列表 | GET | `/api/hrm/job/getJobTitleList` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--获取岗位的表单 | GET | `/api/hrm/job/getJobTitleForm` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--获取查询条件 | GET | `/api/hrm/job/getSearchCondition` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--获取职务岗位树 | GET | `/api/hrm/job/getJobTree` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--获取职务的表单 | GET | `/api/hrm/job/getJobActivityForm` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--获取职务类别列表 | GET | `/api/hrm/job/getJobGroupList` | [人力资源_06.md](人力资源_06.md) |
| 职务岗位设置--获取职务类别的表单 | GET | `/api/hrm/job/getJobGroupForm` | [人力资源_06.md](人力资源_06.md) |
| 职务浏览框-模糊搜索 | GET | `/api/public/browser/complete/282` | [人力资源_06.md](人力资源_06.md) |
| 职务浏览框-高级搜索 | GET | `/api/public/browser/data/282` | [人力资源_06.md](人力资源_06.md) |
| 职务类别--删除职务类别 | POST | `/api/hrm/job/deleteJobGroup` | [人力资源_06.md](人力资源_06.md) |
| 职务类别浏览框-模糊搜索 | GET | `/api/public/browser/complete/281` | [人力资源_06.md](人力资源_06.md) |
| 职务类别浏览框-高级搜索 | GET | `/api/public/browser/data/281` | [人力资源_06.md](人力资源_06.md) |
| 获取人员卡片二维码 | GET | `/api/hrm/resource/getQRCode` | [人力资源_06.md](人力资源_06.md) |
| 获取人员卡片自定义字段左侧树 | GET | `/api/hrm/resourcefielddefined/getTree` | [人力资源_06.md](人力资源_06.md) |
| 获取人员查询结果列表 | POST | `/api/hrm/organization/getResourceSearchList` | [人力资源_06.md](人力资源_06.md) |
| 获取分部列表 | POST | `/api/hrm/organization/getSubCompanySearchList` | [人力资源_06.md](人力资源_06.md) |
| 获取分部自定义字段 | GET | `/api/hrm/subcompanyfielddefined/getFieldDefinedInfo` | [人力资源_06.md](人力资源_06.md) |
| 获取分部表单 | GET | `/api/hrm/organization/getSubCompanyFormField` | [人力资源_06.md](人力资源_06.md) |
| 获取加入虚拟维度表单 | POST | `/api/hrm/organization/getResourceVirtualDepartmentSetFormField` | [人力资源_06.md](人力资源_06.md) |
| 获取单个矩阵打开之后的数据 | POST | `/api/hrm/matrix/pages/matrixList/getMatrixListSetForm` | [人力资源_06.md](人力资源_06.md) |
| 获取工资单管理列表 | POST | `/api/hrm/finance/salarymanage/getSalaryManageList` | [人力资源_06.md](人力资源_06.md) |
| 获取工资单管理列表查询条件 | POST | `/api/hrm/finance/salarymanage/getSalaryManageListCondition` | [人力资源_06.md](人力资源_06.md) |
| 获取工资单管理表单查询条件 | POST | `/api/hrm/finance/salarymanage/getSalaryManageFormCondition` | [人力资源_06.md](人力资源_06.md) |
| 获取总部表单 | GET | `/api/hrm/organization/getCompanyFormField` | [人力资源_07.md](人力资源_07.md) |
| 获取批量设置虚拟维度上级表单 | POST | `/api/hrm/organizationvirtual/getBatchSetManagerFormField` | [人力资源_07.md](人力资源_07.md) |
| 获取批量调整上级分部页面表单 | POST | `/api/hrm/batchMaintenanceAdjustEdit/getBatchSupSubcomid` | [人力资源_07.md](人力资源_07.md) |
| 获取新增人员表单 | GET | `/api/hrm/resource/add/getHrmResourceAddForm` | [人力资源_07.md](人力资源_07.md) |
| 获取权限角色引用表单 | GET | `/api/hrm/systemrightgroup/getSystemRightRolesForm` | [人力资源_07.md](人力资源_07.md) |
| 获取登录人信息 | GET | `/api/hrm/login/getAccountList` | [人力资源_07.md](人力资源_07.md) |
| 获取登录表单 | POST | `/api/hrm/login/getLoginForm` | [人力资源_07.md](人力资源_07.md) |
| 获取矩阵列表数据 | POST | `/api/hrm/matrix/pages/matrixList/getMatrixListSearchList` | [人力资源_07.md](人力资源_07.md) |
| 获取组织图标的各种tab页签查询条件 | POST | `/api/hrm/orgchart/getOrgChartSearchCondition` | [人力资源_07.md](人力资源_07.md) |
| 获取组织图表数据 | POST | `/api/hrm/orgchart/getOrgChartData` | [人力资源_07.md](人力资源_07.md) |
| 获取虚拟组织结构分部查询条件 | GET | `/api/hrm/organizationvirtual/getSubCompanySearchCondition` | [人力资源_07.md](人力资源_07.md) |
| 获取虚拟维度人员列表 | POST | `/api/hrm/organizationvirtual/getResourceSearchList` | [人力资源_07.md](人力资源_07.md) |
| 获取虚拟维度分部信息 | GET | `/api/hrm/organizationvirtual/getSubCompanyFormFieldView` | [人力资源_07.md](人力资源_07.md) |
| 获取虚拟维度分部列表 | POST | `/api/hrm/organizationvirtual/getSubCompanySearchList` | [人力资源_07.md](人力资源_07.md) |
| 获取虚拟维度表单 | GET | `/api/hrm/organizationvirtual/getCompanyFormField` | [人力资源_07.md](人力资源_07.md) |
| 获取虚拟维度部门信息 | GET | `/api/hrm/organizationvirtual/getDepartmentFormFieldView` | [人力资源_07.md](人力资源_07.md) |
| 获取虚拟维度部门列表 | POST | `/api/hrm/organizationvirtual/getDepartmentSearchList` | [人力资源_07.md](人力资源_07.md) |
| 获取虚拟维度部门列表查询条件 | GET | `/api/hrm/organizationvirtual/getDepartmentSearchCondition` | [人力资源_07.md](人力资源_07.md) |
| 获取虚拟维度页签 | POST | `/api/hrm/organizationvirtual/getTabs` | [人力资源_07.md](人力资源_07.md) |
| 获取部门列表 | POST | `/api/hrm/organization/getDepartmentSearchList` | [人力资源_07.md](人力资源_07.md) |
| 获取部门自定义字段 | GET | `/api/hrm/departmentfielddefined/getFieldDefinedInfo` | [人力资源_07.md](人力资源_07.md) |
| 获取部门表单 | GET | `/api/hrm/organization/getDepartmentFormField` | [人力资源_07.md](人力资源_07.md) |
| 虚拟维度人员列表查询条件 | GET | `/api/hrm/organizationvirtual/getResourceSearchCondition` | [人力资源_07.md](人力资源_07.md) |
| 虚拟维度分部表单 | GET | `/api/hrm/organizationvirtual/getSubCompanyFormField` | [人力资源_07.md](人力资源_07.md) |
| 虚拟维度右键菜单 | POST | `/api/hrm/organizationvirtual/getRightMenu` | [人力资源_07.md](人力资源_07.md) |
| 虚拟维度批量设置上级保存 | POST | `/api/hrm/organizationvirtual/saveBatchSetManager` | [人力资源_07.md](人力资源_07.md) |
| 角色功能权限列表 | POST | `/api/hrm/rolefucrightset/getRolesFucRightSetList` | [人力资源_07.md](人力资源_07.md) |
| 角色功能权限查询条件 | GET | `/api/hrm/rolefucrightset/getRolesFucRightSetCondition` | [人力资源_07.md](人力资源_07.md) |
| 角色功能权限表单 | GET | `/api/hrm/rolefucrightset/getRolesFucRightSetForm` | [人力资源_07.md](人力资源_07.md) |
| 角色权限查询条件 | GET | `/api/hrm/rolesstrrightset/getRolesStrRightSetCondition` | [人力资源_07.md](人力资源_07.md) |
| 角色设置权限判断 | POST | `/api/hrm/role/getHasRight` | [人力资源_08.md](人力资源_08.md) |
| 解封分部 | POST | `/api/hrm/organization/doSubCompanyISCanceled` | [人力资源_08.md](人力资源_08.md) |
| 解封虚拟维度分部 | POST | `/api/hrm/organizationvirtual/doSubCompanyISCanceled` | [人力资源_08.md](人力资源_08.md) |
| 解封虚拟维度部门 | POST | `/api/hrm/organizationvirtual/doDepartmentISCanceled` | [人力资源_08.md](人力资源_08.md) |
| 解封部门 | POST | `/api/hrm/organization/doDepartmentISCanceled` | [人力资源_08.md](人力资源_08.md) |
| 通讯录--保存默认排序设置 | POST | `/api/hrm/search/saveOrderBy4Search` | [人力资源_08.md](人力资源_08.md) |
| 通讯录--获取人员列表 | POST | `/api/hrm/search/getHrmSearchResult` | [人力资源_08.md](人力资源_08.md) |
| 通讯录--获取高级搜索查询条件 | GET | `/api/hrm/search/getHrmSearchCondition` | [人力资源_08.md](人力资源_08.md) |
| 通讯录--获取默认排序设置 | GET | `/api/hrm/search/getOrderBy4Search` | [人力资源_08.md](人力资源_08.md) |
| 部门列表查询条件 | GET | `/api/hrm/organization/getDepartmentSearchCondition` | [人力资源_08.md](人力资源_08.md) |
| 部门浏览框-模糊搜索 | GET | `/api/public/browser/complete/4` | [人力资源_08.md](人力资源_08.md) |
| 部门浏览框-高级搜索 | GET | `/api/public/browser/data/4` | [人力资源_08.md](人力资源_08.md) |
| 部门自定义字段删除接口 | POST | `/api/hrm/departmentfielddefined/del` | [人力资源_08.md](人力资源_08.md) |
| 部门自定义字段移动分组 | POST | `/api/hrm/departmentfielddefined/changegroup` | [人力资源_08.md](人力资源_08.md) |
| 部门自定义字段页签 | GET | `/api/hrm/departmentfielddefined/getTabInfo` | [人力资源_08.md](人力资源_08.md) |

## 工作流程

| 接口 | 方法 | 地址 | 文件 |
|---|---|---|---|
| 流程实例：删除流程（对外） | POST | `/api/workflow/paService/deleteRequest` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：强制归档（对外） | POST | `/api/workflow/paService/doForceOver` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：强制收回（对外） | POST | `/api/workflow/paService/doForceDrawBack` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：意见保存(对外) | POST | `/api/workflow/paService/saveRequestLog` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：提交(对外) | POST | `/api/workflow/paService/submitRequest` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：新建(对外) | POST | `/api/workflow/paService/doCreateRequest` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：流程干预（对外） | POST | `/api/workflow/paService/doIntervenor` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：流程撤回（对外） | POST | `/api/workflow/paService/withdrawRequest` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：获取流程信息（对外） | GET | `/api/workflow/paService/getWorkflowRequest` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：获取流程图链接(对外) | GET | `/api/workflow/paService/getRequestFlowChart` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：获取流程意见（对外） | GET | `/api/workflow/paService/getRequestLog` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：获取流程流转数据（对外） | GET | `/api/workflow/paService/getRequestOperatorInfo` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：获取流程状态数据（对外） | GET | `/api/workflow/paService/getRequestStatus` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：获取流程相关资源(对外) | GET | `/api/workflow/paService/getRequestResources` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：转发、意见征询、转办(对外) | POST | `/api/workflow/paService/forwardRequest` | [工作流程_01.md](工作流程_01.md) |
| 流程实例：退回(对外) | POST | `/api/workflow/paService/rejectRequest` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：办结流程列表 (对外) | POST | `/api/workflow/paService/getProcessedWorkflowRequestList` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：办结流程数量 (对外) | POST | `/api/workflow/paService/getProcessedWorkflowRequestCount` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：可创建流程类型数量 (对外) | POST | `/api/workflow/paService/getCreateWorkflowTypeCount` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：可创建的流程列表 (对外) | POST | `/api/workflow/paService/getCreateWorkflowList` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：可创建的流程数量 (对外) | POST | `/api/workflow/paService/getCreateWorkflowCount` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：可创建的流程类型列表 (对外) | POST | `/api/workflow/paService/getCreateWorkflowTypeList` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：已办流程列表(不包含异构系统数据) (对外) | POST | `/api/workflow/paService/getHandledWorkflowRequestList` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：已办流程列表(可选择是否包含异构系统数据) (对外) | POST | `/api/workflow/paService/getHandledWorkflowRequestList4Ofs` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：已办流程数量(不包含异构系统数据) (对外) | POST | `/api/workflow/paService/getHandledWorkflowRequestCount` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：已办流程数量(可选择是否包含异构系统数据) (对外) | POST | `/api/workflow/paService/getHandledWorkflowRequestCount4Ofs` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：待办 中抄送流程数量 (对外) | POST | `/api/workflow/paService/getCCWorkflowRequestCount` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：待办中抄送流程列表 (对外) | POST | `/api/workflow/paService/getCCWorkflowRequestList` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：待办中退回流程列表 (对外) | POST | `/api/workflow/paService/getBeRejectWorkflowRequestList` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：待办中退回流程数量 (对外) | POST | `/api/workflow/paService/getBeRejectWorkflowRequestCount` | [工作流程_01.md](工作流程_01.md) |
| 流程数据：待办列表数量 (对外) | POST | `/api/workflow/paService/getToDoWorkflowRequestCount` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：待办流程列表 (对外) | POST | `/api/workflow/paService/getToDoWorkflowRequestList` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：待处理流程列表 (对外) | POST | `/api/workflow/paService/getDoingWorkflowRequestList` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：待处理流程数量 (对外) | POST | `/api/workflow/paService/getDoingWorkflowRequestCount` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：待阅流程列表 (对外) | POST | `/api/workflow/paService/getToBeReadWorkflowRequestList` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：待阅流程数量 (对外) | POST | `/api/workflow/paService/getToBeReadWorkflowRequestCount` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：所发起流程列表 (对外) | POST | `/api/workflow/paService/getMyWorkflowRequestList` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：所发起流程数量 (对外) | POST | `/api/workflow/paService/getMyWorkflowRequestCount` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：所有流程列表 (对外) | POST | `/api/workflow/paService/getAllWorkflowRequestList` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：所有流程数量 (对外) | POST | `/api/workflow/paService/getAllWorkflowRequestCount` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：根据 tabids 来获取流程列表 (对外) | POST | `/api/workflow/paService/getToDoRequestList` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：根据tabids来获取流程数量 (对外) | POST | `/api/workflow/paService/getToDoRequestCount` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：流程签字意见 (对外) | POST | `/api/workflow/paService/getWorkflowRequestLogs` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：转发流程列表(只统计还在待办的) (对外) | POST | `/api/workflow/paService/getForwardWorkflowRequestList` | [工作流程_02.md](工作流程_02.md) |
| 流程数据：转发流程数量(只统计还在待办的) (对外) | POST | `/api/workflow/paService/getForwardWorkflowRequestCount` | [工作流程_02.md](工作流程_02.md) |

## 知识管理

| 接口 | 方法 | 地址 | 文件 |
|---|---|---|---|
| 创建文档总数 | GET | `/api/doc/categoryReport/docNum` | [知识管理_01.md](知识管理_01.md) |
| 删除文档 | GET | `/api/doc/operate/delete` | [知识管理_01.md](知识管理_01.md) |
| 删除文档评论-em7 | GET | `/api/doc/mobile/systemDoc/deleteReply` | [知识管理_01.md](知识管理_01.md) |
| 删除默认共享 | POST | `/api/doc/console/category/defaultRight/delete` | [知识管理_01.md](知识管理_01.md) |
| 回复列表-em7 | GET | `/api/doc/mobile/systemDoc/getReply` | [知识管理_01.md](知识管理_01.md) |
| 回收站-文档列表 | GET | `/api/doc/recycle/list` | [知识管理_01.md](知识管理_01.md) |
| 失效文档 | GET | `/api/doc/detail/invalidate` | [知识管理_01.md](知识管理_01.md) |
| 导入文档到虚拟目录 | GET | `/api/doc/operate/import2Dummy` | [知识管理_01.md](知识管理_01.md) |
| 批量调整共享 | POST | `/api/doc/share/saveShareBatch` | [知识管理_01.md](知识管理_01.md) |
| 文档共享列表 | GET | `/api/doc/share/list` | [知识管理_01.md](知识管理_01.md) |
| 文档回复-保存 | POST | `/api/doc/reply/saveReply` | [知识管理_01.md](知识管理_01.md) |
| 文档回复-回复列表 | GET | `/api/doc/reply/replyList` | [知识管理_01.md](知识管理_01.md) |
| 文档回复数 | GET | `/api/doc/reply/replyCount` | [知识管理_01.md](知识管理_01.md) |
| 文档回复评论接口-em7 | GET | `/api/doc/mobile/systemDoc/replyDoc` | [知识管理_01.md](知识管理_01.md) |
| 文档总数 | GET | `/api/doc/report/createDocNum` | [知识管理_01.md](知识管理_01.md) |
| 文档置顶 | GET | `/api/doc/detail/setTop` | [知识管理_01.md](知识管理_01.md) |
| 文档详情-tab页 | GET | `/api/doc/detail/tabInfo` | [知识管理_01.md](知识管理_01.md) |
| 文档详情-基本信息 | GET | `/api/doc/detail/basicInfo` | [知识管理_01.md](知识管理_01.md) |
| 文档详情-打分 | GET | `/api/doc/score/doMarkDoc` | [知识管理_01.md](知识管理_01.md) |
| 文档详情-打分信息 | GET | `/api/doc/score/docScore` | [知识管理_01.md](知识管理_01.md) |
| 文档详情-文档内容 | GET | `/api/doc/detail/htmlContent` | [知识管理_01.md](知识管理_01.md) |
| 文档详情-文档属性 | GET | `/api/doc/detail/docParamInfo` | [知识管理_01.md](知识管理_01.md) |
| 文档详情-文档版本 | GET | `/api/doc/detail/docVersion` | [知识管理_01.md](知识管理_01.md) |
| 文档详情-有附件时展开文档附件属性附件列表 | GET | `/api/doc/detail/docAutoExtendInfo` | [知识管理_01.md](知识管理_01.md) |
| 文档详情-添加文档阅读记录 | GET | `/api/doc/read/addReadLog` | [知识管理_01.md](知识管理_01.md) |
| 文档详情-点赞信息 | GET | `/api/doc/praise/praiseInfo` | [知识管理_01.md](知识管理_01.md) |
| 新建、编辑文档-保存 | POST | `/api/doc/save/save` | [知识管理_01.md](知识管理_01.md) |
| 新建、编辑文档-提交 | POST | `/api/doc/save/submit` | [知识管理_01.md](知识管理_01.md) |
| 新建、编辑文档-是否签出验证 | GET | `/api/doc/save/isCheckOut` | [知识管理_01.md](知识管理_01.md) |
| 新建、编辑文档-根据附件生成一篇文档 | GET | `/api/doc/save/accForDoc` | [知识管理_01.md](知识管理_01.md) |
| 新建、编辑文档-附件列表 | GET | `/api/doc/save/getAccListForEdit` | [知识管理_02.md](知识管理_02.md) |
| 新建文档-(取消)收藏目录 | GET | `/api/doc/category/collute` | [知识管理_02.md](知识管理_02.md) |
| 新建文档-目录树 | GET | `/api/doc/category/treeNode` | [知识管理_02.md](知识管理_02.md) |
| 替换附件 | GET | `/api/doc/acc/docAccReplace` | [知识管理_02.md](知识管理_02.md) |
| 查看新闻页列表 | GET | `/api/doc/console/news/table` | [知识管理_02.md](知识管理_02.md) |
| 查阅文档-文档列表 | GET | `/api/doc/searchlist/list` | [知识管理_02.md](知识管理_02.md) |
| 添加文档共享 | POST | `/api/doc/share/saveShare` | [知识管理_02.md](知识管理_02.md) |
| 点赞 | GET | `/api/doc/praise/doPraise` | [知识管理_02.md](知识管理_02.md) |
| 点赞、取消点赞-em7 | POST | `/api/doc/mobile/systemDoc/praiseDoc` | [知识管理_02.md](知识管理_02.md) |
| 登录前新闻-html文档正文 | GET | `/api/doc/out/detail/docContent` | [知识管理_02.md](知识管理_02.md) |
| 登录前门户-列表 | GET | `/api/doc/out/more/list` | [知识管理_02.md](知识管理_02.md) |
| 目录列表 | GET | `/api/doc/console/category/table` | [知识管理_02.md](知识管理_02.md) |
| 目录树查询接口 | GET | `/api/doc/console/category/tree` | [知识管理_02.md](知识管理_02.md) |
| 知识中心-上传文档 | GET | `/api/doc/doccenter/getUploadSet` | [知识管理_02.md](知识管理_02.md) |
| 知识中心-我的小伙伴们都在看什么（Tab页） | GET | `/api/doc/doccenter/tabInfoOfPartner` | [知识管理_02.md](知识管理_02.md) |
| 编辑新闻 | POST | `/api/doc/console/news/update` | [知识管理_02.md](知识管理_02.md) |
| 获取全部文档列表-em7 | GET | `/api/doc/mobile/systemDoc/getAllDocList` | [知识管理_02.md](知识管理_02.md) |
| 获取我的收藏文档列表-em7 | GET | `/api/doc/mobile/systemDoc/getCollectDocList` | [知识管理_02.md](知识管理_02.md) |
| 获取我的文档列表-em7 | GET | `/api/doc/mobile/systemDoc/getMyDocList` | [知识管理_02.md](知识管理_02.md) |
| 获取指定目录下的文档列表-em7 | GET | `/api/doc/mobile/systemDoc/getCategoryDocList` | [知识管理_02.md](知识管理_02.md) |
| 获取新闻信息 | GET | `/api/doc/console/news/info` | [知识管理_02.md](知识管理_02.md) |
| 获取新闻图库列表 | GET | `/api/doc/console/news/pic/table` | [知识管理_02.md](知识管理_02.md) |
| 获取目录列表集合-em7 | GET | `/api/doc/mobile/systemDoc/getCategoryList` | [知识管理_02.md](知识管理_02.md) |
| 获取默认的权限列表 | GET | `/api/doc/console/category/defaultRight` | [知识管理_02.md](知识管理_02.md) |
| 调整所有共享 | POST | `/api/doc/console/multi/share/entire` | [知识管理_02.md](知识管理_02.md) |
| 附件上传 | POST | `/api/doc/upload/uploadFile` | [知识管理_02.md](知识管理_02.md) |
| 附件上传 | POST | `/api/doc/upload/uploadFile2Doc` | [知识管理_02.md](知识管理_02.md) |
| 附件列表 | GET | `/api/doc/acc/docAcc` | [知识管理_02.md](知识管理_02.md) |
| 附件版本列表 | GET | `/api/doc/acc/docAccVersion` | [知识管理_02.md](知识管理_02.md) |
| 附件重命名 | POST | `/api/doc/acc/rename` | [知识管理_02.md](知识管理_02.md) |

## 考勤

| 接口 | 方法 | 地址 | 文件 |
|---|---|---|---|
| 一键启用考勤--初始化 | GET | `/api/kq/setupwizard/performInitialization` | [考勤_01.md](考勤_01.md) |
| 一键启用考勤--判断是否具有权限 | GET | `/api/kq/setupwizard/getHasRight` | [考勤_01.md](考勤_01.md) |
| 一键启用考勤--获取单个步骤 | GET | `/api/kq/setupwizard/getSetupSteps` | [考勤_01.md](考勤_01.md) |
| 一键启用考勤--获取表单 | GET | `/api/kq/setupwizard/getSetupForm` | [考勤_01.md](考勤_01.md) |
| 一键启用考勤-右键菜单 | GET | `/api/kq/setupwizard/getRightMenu` | [考勤_01.md](考勤_01.md) |
| 保存考勤流程设置的 字段对应信息 | POST | `/api/kq/wfSetting/statesShedule/saveStateProcSetFlowWfFields` | [考勤_01.md](考勤_01.md) |
| 保存考勤流程设置的 流程概览 | POST | `/api/kq/wfSetting/statesShedule/saveStateProcSetFlow` | [考勤_01.md](考勤_01.md) |
| 假期余额--保存修改 | POST | `/api/kq/balanceofleave/saveBalanceOfLeave` | [考勤_01.md](考勤_01.md) |
| 假期类型--保存启用/不启用的假期类型 | POST | `/api/kq/leavetypes/saveDisableLeaveTypes` | [考勤_01.md](考勤_01.md) |
| 假期类型--删除 | POST | `/api/kq/leavetypes/deleteLeaveTypes` | [考勤_01.md](考勤_01.md) |
| 假期类型--判断是否有权限 | GET | `/api/kq/leavetypes/getHasRight` | [考勤_01.md](考勤_01.md) |
| 假期类型--新建假期类型 | POST | `/api/kq/leavetypes/addLeaveTypes` | [考勤_01.md](考勤_01.md) |
| 假期类型--编辑假期类型 | POST | `/api/kq/leavetypes/editLeaveTypes` | [考勤_01.md](考勤_01.md) |
| 假期类型--获取假期类型列表 | GET | `/api/kq/leavetypes/getSearchList` | [考勤_01.md](考勤_01.md) |
| 假期类型--获取右键菜单 | GET | `/api/kq/leavetypes/getRightMenu` | [考勤_01.md](考勤_01.md) |
| 假期类型--获取新建或编辑的表单 | GET | `/api/kq/leavetypes/getLeaveTypesForm` | [考勤_01.md](考勤_01.md) |
| 假期类型--获取查询条件 | GET | `/api/kq/leavetypes/getSearchCondition` | [考勤_01.md](考勤_01.md) |
| 假期规则--删除 | POST | `/api/kq/leaverules/deleteLeaveRules` | [考勤_01.md](考勤_01.md) |
| 假期规则--判断是否权限 | GET | `/api/kq/leaverules/getHasRight` | [考勤_01.md](考勤_01.md) |
| 假期规则--新建假期规则 | POST | `/api/kq/leaverules/addLeaveRules` | [考勤_01.md](考勤_01.md) |
| 假期规则--编辑 | POST | `/api/kq/leaverules/editLeaveRules` | [考勤_01.md](考勤_01.md) |
| 假期规则--获取假期类型的请假时长的单位 | GET | `/api/kq/leaverules/getUnitName` | [考勤_01.md](考勤_01.md) |
| 假期规则--获取假期规则的列表 | GET | `/api/kq/leaverules/getSearchList` | [考勤_01.md](考勤_01.md) |
| 假期规则--获取右键菜单 | GET | `/api/kq/leaverules/getRightMenu` | [考勤_01.md](考勤_01.md) |
| 假期规则--获取新建或者编辑的表单 | GET | `/api/kq/leaverules/getLeaveRulesForm` | [考勤_01.md](考勤_01.md) |
| 假期规则--获取高级搜索的表单 | GET | `/api/kq/leaverules/getSearchCondition` | [考勤_01.md](考勤_01.md) |
| 公出出差规则--保存 | POST | `/api/kq/travelrules/saveTravelRules` | [考勤_01.md](考勤_01.md) |
| 公出出差规则--判断是否有权限 | GET | `/api/kq/travelrules/getHasRight` | [考勤_01.md](考勤_01.md) |
| 公出出差规则--获取右键菜单 | GET | `/api/kq/travelrules/getRightMenu` | [考勤_01.md](考勤_01.md) |
| 公出出差规则--获取表单 | GET | `/api/kq/travelrules/getTravelRulesForm` | [考勤_01.md](考勤_01.md) |
| 删除考勤流程设置 | POST | `/api/kq/wfSetting/statesShedule/delStateProcSet` | [考勤_02.md](考勤_02.md) |
| 加班规则--保存加班单位的设置 | POST | `/api/kq/overtimerules/saveOvertimeUnit` | [考勤_02.md](考勤_02.md) |
| 加班规则--删除 | POST | `/api/kq/overtimerules/deleteOvertimeRules` | [考勤_02.md](考勤_02.md) |
| 加班规则--判断是否有权限 | GET | `/api/kq/overtimerules/getHasRight` | [考勤_02.md](考勤_02.md) |
| 加班规则--新建加班规则 | POST | `/api/kq/overtimerules/addOvertimeRules` | [考勤_02.md](考勤_02.md) |
| 加班规则--编辑加班规则 | POST | `/api/kq/overtimerules/editOvertimeRules` | [考勤_02.md](考勤_02.md) |
| 加班规则--获取加班单位的表单 | GET | `/api/kq/overtimerules/getOvertimeUnitForm` | [考勤_02.md](考勤_02.md) |
| 加班规则--获取加班规则的列表 | GET | `/api/kq/overtimerules/getSearchList` | [考勤_02.md](考勤_02.md) |
| 加班规则--获取加班规则的右键菜单 | GET | `/api/kq/overtimerules/getRightMenu` | [考勤_02.md](考勤_02.md) |
| 加班规则--获取加班规则的新建或编辑的表单 | GET | `/api/kq/overtimerules/getOvertimeRulesForm` | [考勤_02.md](考勤_02.md) |
| 原始打卡记录--判断是否有权限 | GET | `/api/kq/originalpunchrp/getHasRight` | [考勤_02.md](考勤_02.md) |
| 原始打卡记录--获取右键菜单 | GET | `/api/kq/originalpunchrp/getRightMenu` | [考勤_02.md](考勤_02.md) |
| 原始打卡记录--获取报表数据 | GET | `/api/kq/originalpunchrp/getSearchList` | [考勤_02.md](考勤_02.md) |
| 原始打卡记录报表--获取高级搜索 | GET | `/api/kq/originalpunchrp/getSearchCondition` | [考勤_02.md](考勤_02.md) |
| 员工假期余额--判断是否具有权限 | GET | `/api/kq/balanceofleave/getHasRight` | [考勤_02.md](考勤_02.md) |
| 员工假期余额--导入员工假期余额 | POST | `/api/kq/balanceofleave/saveImport` | [考勤_02.md](考勤_02.md) |
| 员工假期余额--获取TAB页签 | GET | `/api/kq/balanceofleave/getTabs` | [考勤_02.md](考勤_02.md) |
| 员工假期余额--获取右键菜单 | GET | `/api/kq/balanceofleave/getRightMenu` | [考勤_02.md](考勤_02.md) |
| 员工假期余额--获取员工假期余额列表 | GET | `/api/kq/balanceofleave/getSearchList` | [考勤_02.md](考勤_02.md) |
| 员工假期余额--获取高级搜索的查询条件 | GET | `/api/kq/balanceofleave/getSearchCondition` | [考勤_02.md](考勤_02.md) |
| 员工假期余额-判断是否具有权限 | GET | `/api/kq/balanceofleaverp/getHasRight` | [考勤_02.md](考勤_02.md) |
| 员工假期余额-批处理 | POST | `/api/kq/balanceofleave/batchProcessing` | [考勤_02.md](考勤_02.md) |
| 员工假期余额-获取导入表单 | GET | `/api/kq/balanceofleave/getImportForm` | [考勤_02.md](考勤_02.md) |
| 员工假期余额报表--使用记录--获取分页数据 | GET | `/api/kq/balanceofleaverp/getDetailPageInfo` | [考勤_02.md](考勤_02.md) |
| 员工假期余额报表--使用记录--获取记录变更类型 | GET | `/api/kq/balanceofleaverp/getChangeType` | [考勤_02.md](考勤_02.md) |
| 员工假期余额报表--使用记录一共有多少页签 | GET | `/api/kq/balanceofleaverp/getTab` | [考勤_02.md](考勤_02.md) |
| 员工假期余额报表--获取使用记录 | GET | `/api/kq/balanceofleaverp/getUsageRecordDetail` | [考勤_02.md](考勤_02.md) |
| 员工假期余额报表--获取分页信息 | GET | `/api/kq/balanceofleaverp/getPageInfo` | [考勤_02.md](考勤_02.md) |
| 员工假期余额报表--获取右键菜单 | GET | `/api/kq/balanceofleaverp/getRightMenu` | [考勤_02.md](考勤_02.md) |
| 员工假期余额报表--获取报表数据 | GET | `/api/kq/balanceofleaverp/getSearchList` | [考勤_02.md](考勤_02.md) |
| 员工假期余额报表-获取高级搜索 | GET | `/api/kq/balanceofleaverp/getSearchCondition` | [考勤_03.md](考勤_03.md) |
| 我的考勤--考勤明细 | POST | `/api/kq/myattendance/getHrmKQReportDetialInfo` | [考勤_03.md](考勤_03.md) |
| 我的考勤--考勤统计 | POST | `/api/kq/myattendance/getHrmKQReportInfo` | [考勤_03.md](考勤_03.md) |
| 我的考勤--获取日历模式下的数据 | POST | `/api/kq/myattendance/getHrmKQMonthReportInfo` | [考勤_03.md](考勤_03.md) |
| 我的考勤--获取签到签退数据 | POST | `/api/kq/myattendance/getHrmKQSignInfo` | [考勤_03.md](考勤_03.md) |
| 空 | POST | `/api/kq/balanceofleaverp/exportExcel` | [考勤_03.md](考勤_03.md) |
| 考勤导入--获取导入历史记录 | GET | `/api/kq/importlog/getImportHistory` | [考勤_03.md](考勤_03.md) |
| 考勤导入--获取导入日志 | GET | `/api/kq/importlog/getImportColResultLog` | [考勤_03.md](考勤_03.md) |
| 考勤导入--获取导入结果 | GET | `/api/kq/importlog/getImportResult` | [考勤_03.md](考勤_03.md) |
| 考勤导入--获取导入进行明细 | GET | `/api/kq/importlog/getImportProcessLog` | [考勤_03.md](考勤_03.md) |
| 考勤报表右键菜单 | GET | `/api/kq/report/getRightMenu` | [考勤_03.md](考勤_03.md) |
| 考勤报表导出 | POST | `/api/kq/report/exportExcel` | [考勤_03.md](考勤_03.md) |
| 考勤报表异常明细 | POST | `/api/kq/report/detail/getKQReportDetail` | [考勤_03.md](考勤_03.md) |
| 考勤报表异常明细页签 | POST | `/api/kq/report/detail/getTabs` | [考勤_03.md](考勤_03.md) |
| 考勤报表明细 | POST | `/api/kq/report/detail/getDailyDetialInfo` | [考勤_03.md](考勤_03.md) |
| 考勤报表权限共享--保存 | POST | `/api/kq/reportshare/saveReportShare` | [考勤_03.md](考勤_03.md) |
| 考勤报表权限共享--删除 | POST | `/api/kq/reportshare/deleteReportShare` | [考勤_03.md](考勤_03.md) |
| 考勤报表权限共享--判断是否有权限 | GET | `/api/kq/reportshare/getHasRight` | [考勤_03.md](考勤_03.md) |
| 考勤报表权限共享--获取列表 | GET | `/api/kq/reportshare/getSearchList` | [考勤_03.md](考勤_03.md) |
| 考勤报表权限共享--获取右键菜单 | GET | `/api/kq/reportshare/getRightMenu` | [考勤_03.md](考勤_03.md) |
| 考勤报表权限共享--获取表单 | GET | `/api/kq/reportshare/getReportShareForm` | [考勤_03.md](考勤_03.md) |
| 考勤报表权限共享--获取高级搜索表单 | GET | `/api/kq/reportshare/getSearchCondition` | [考勤_03.md](考勤_03.md) |
| 考勤报表查询条件 | POST | `/api/kq/report/getSearchCondition` | [考勤_03.md](考勤_03.md) |
| 自动创建考勤流程设置表单 | POST | `/api/kq/wfSetting/statesShedule/saveStateProcSetCreateForm` | [考勤_03.md](考勤_03.md) |
| 节假日设置--保存导入的数据 | POST | `/api/kq/holidayset/saveImport` | [考勤_03.md](考勤_03.md) |
| 节假日设置--初始化节假日设置 | POST | `/api/kq/holidayset/initHolidaySet` | [考勤_03.md](考勤_03.md) |
| 节假日设置--删除节假日设置 | POST | `/api/kq/holidayset/deleteHolidaySet` | [考勤_03.md](考勤_03.md) |
| 节假日设置--判断是否有权限 | GET | `/api/kq/holidayset/getHasRight` | [考勤_03.md](考勤_03.md) |
| 节假日设置--同步节假日设置 | POST | `/api/kq/holidayset/syncHolidaySet` | [考勤_03.md](考勤_03.md) |
| 节假日设置--新建节假日设置 | POST | `/api/kq/holidayset/addHolidaySet` | [考勤_03.md](考勤_03.md) |
| 节假日设置--日历 | GET | `/api/kq/holidayset/getHolidaySetCalendar` | [考勤_04.md](考勤_04.md) |
| 节假日设置--统计节假日设置数据 | GET | `/api/kq/holidayset/getHolidayCount` | [考勤_04.md](考勤_04.md) |
| 节假日设置--编辑节假日设置 | POST | `/api/kq/holidayset/editHolidaySet` | [考勤_04.md](考勤_04.md) |
| 节假日设置--获取右键菜单 | GET | `/api/kq/holidayset/getRightMenu` | [考勤_04.md](考勤_04.md) |
| 节假日设置--获取同步的表单 | GET | `/api/kq/holidayset/getSyncForm` | [考勤_04.md](考勤_04.md) |
| 节假日设置--获取导入的表单 | GET | `/api/kq/holidayset/getImportForm` | [考勤_04.md](考勤_04.md) |
| 节假日设置--获取新建或者编辑的表单 | GET | `/api/kq/holidayset/getHolidaySetForm` | [考勤_04.md](考勤_04.md) |
| 节假日设置--获取节假日设置的列表 | GET | `/api/kq/holidayset/getSearchList` | [考勤_04.md](考勤_04.md) |
| 获取考勤报表 | POST | `/api/kq/report/getKQReport` | [考勤_04.md](考勤_04.md) |
| 获取考勤流程设置 动作设置 | POST | `/api/kq/wfSetting/statesShedule/getStateProcSetFlowWfSet` | [考勤_04.md](考勤_04.md) |
| 获取考勤流程设置 字段对应信息 | POST | `/api/kq/wfSetting/statesShedule/getStateProcSetFlowWfFields` | [考勤_04.md](考勤_04.md) |
| 获取考勤流程设置 流程概览信息 | POST | `/api/kq/wfSetting/statesShedule/getStateProcSetFlowForm` | [考勤_04.md](考勤_04.md) |
| 获取考勤流程设置的 tab页签数据 | POST | `/api/kq/wfSetting/statesShedule/getStateProcSetTabInfo` | [考勤_04.md](考勤_04.md) |
| 获取考勤流程设置的查询列表 | POST | `/api/kq/wfSetting/statesShedule/getStateProcSetListSearchList` | [考勤_04.md](考勤_04.md) |
| 获取考勤流程设置的查询条件 | GET | `/api/kq/wfSetting/statesShedule/getStateProcSetListSearchCondition` | [考勤_04.md](考勤_04.md) |
| 调休--判断是否有权限 | GET | `/api/kq/tiaoxiu/getHasRight` | [考勤_04.md](考勤_04.md) |
| 重新计算考勤报表 | POST | `/api/kq/report/format` | [考勤_04.md](考勤_04.md) |

## 门户管理

| 接口 | 方法 | 地址 | 文件 |
|---|---|---|---|
| 【文档中心】元素创建文档按钮权限判断接口 | POST | `/api/portal/elementsetdoc/docsetright` | [门户管理_01.md](门户管理_01.md) |
| 前端门户页面获取页面以及元素数据列表接口 | POST | `/api/portal/homepage/hpdata` | [门户管理_01.md](门户管理_01.md) |
| 获取【图表】元素sql模板库设置页面信息 | POST | `/api/portal/sqltemplate/datas` | [门户管理_01.md](门户管理_01.md) |
| 获取主题配置 | GET | `/api/portal/themeConfig/getThemeConfig` | [门户管理_01.md](门户管理_01.md) |
| 获取任务元素设置信息和数据方法 | POST | `/api/portal/element/task` | [门户管理_01.md](门户管理_01.md) |
| 获取任务元素设置信息和数据方法 | POST | `/api/portal/element/tasktab` | [门户管理_01.md](门户管理_01.md) |
| 获取任务计划元素设置信息和数据方法 | POST | `/api/portal/element/worktask` | [门户管理_01.md](门户管理_01.md) |
| 获取元素tab数据 | GET | `/api/mobile/portal/elements/tab` | [门户管理_01.md](门户管理_01.md) |
| 获取元素设置页面数据接口 | POST | `/api/portal/setting/esetting` | [门户管理_01.md](门户管理_01.md) |
| 获取前端菜单信息 | GET | `/api/portal/menu/getFrontEndMenu` | [门户管理_01.md](门户管理_01.md) |
| 获取后台菜单信息接口 | GET | `/api/portal/menu/getBackEndMenu` | [门户管理_01.md](门户管理_01.md) |
| 获取多新闻中心元素设置信息和数据方法 | POST | `/api/portal/element/morenews` | [门户管理_01.md](门户管理_01.md) |
| 获取多新闻中心元素设置信息和数据方法 | POST | `/api/portal/element/coremail` | [门户管理_01.md](门户管理_01.md) |
| 获取工具栏更多菜单 | GET | `/api/portal/toolbarMore/getToolbarMoreMenu` | [门户管理_01.md](门户管理_01.md) |
| 获取工具栏菜单 | GET | `/api/portal/toolbar/getToolbarMenu` | [门户管理_01.md](门户管理_01.md) |
| 获取当前账号和多账号列表 | GET | `/api/portal/account/getAccount` | [门户管理_01.md](门户管理_01.md) |
| 获取快捷搜索类型 | GET | `/api/portal/quickSearch/getQuickSearchTypes` | [门户管理_01.md](门户管理_01.md) |
| 获取快捷搜索类型 | GET | `/api/portal/quickSearchMaintenance/getQuickSearchTypes` | [门户管理_01.md](门户管理_01.md) |
| 获取我的主题 | GET | `/api/portal/themeCenter/getMyTheme` | [门户管理_01.md](门户管理_01.md) |
| 获取用户常用菜单数据 | POST | `/api/portal/frequsemenu/getdata` | [门户管理_01.md](门户管理_01.md) |
| 获取登录前门户信息 | POST | `/api/portal/login/logininfo` | [门户管理_01.md](门户管理_01.md) |
| 获取系统版本 | GET | `/api/portal/systemInfo/getVersion` | [门户管理_01.md](门户管理_01.md) |
| 获取账号菜单 | GET | `/api/portal/account/getAccountMenu` | [门户管理_01.md](门户管理_01.md) |
| 获取通告栏元素设置信息和数据方法 | POST | `/api/portal/element/notice` | [门户管理_01.md](门户管理_01.md) |
| 获取门户【RSS】元素列表信息 | POST | `/api/portal/element/rsstab` | [门户管理_01.md](门户管理_01.md) |
| 获取门户【RSS】元素列表信息 | POST | `/api/portal/element/rss` | [门户管理_01.md](门户管理_01.md) |
| 获取门户【个人数据】元素列表信息 | POST | `/api/portal/element/datacenter` | [门户管理_01.md](门户管理_01.md) |
| 获取门户【人员看板元素】信息 | POST | `/api/portal/element/hdpanel/getListData` | [门户管理_01.md](门户管理_01.md) |
| 获取门户【人员看板元素】设置信息 | POST | `/api/portal/element/hdpanel/getSettingDate` | [门户管理_01.md](门户管理_01.md) |
| 获取门户【会议日历】元素信息 | POST | `/api/portal/element/meetingCalendar` | [门户管理_01.md](门户管理_01.md) |
| 获取门户【便签元素】元素列表信息 | POST | `/api/portal/element/scratchpad` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【公司新闻】元素信息 | POST | `/api/portal/element/loginnewstab` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【公司新闻】元素信息 | POST | `/api/portal/element/loginnews` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【公告元素】元素信息 | POST | `/api/portal/element/newnotice` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【图片元素】列表信息 | POST | `/api/portal/element/picture` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【图表元素】元素列表信息 | POST | `/api/portal/element/reportformtab` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【图表元素】元素列表信息 | POST | `/api/portal/element/reportform` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【外部数据元素】列表信息 | POST | `/api/portal/element/outdatatab` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【外部数据元素】列表信息 | POST | `/api/portal/element/outdata` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【多图元素】信息 | POST | `/api/portal/element/imgslide` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【多岗位办理事项】元素信息 | POST | `/api/portal/element/jobsinfo` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【天气元素】元素列表信息 | POST | `/api/portal/element/weather` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【幻灯片】元素列表信息 | POST | `/api/portal/element/slide` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【建模查询中心】列表信息 | POST | `/api/portal/element/formmodecustomsearch` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【建模查询中心】列表信息 | POST | `/api/portal/element/formmodecustomsearchtab` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【当日计划】元素列表信息 | POST | `/api/portal/element/dayplan` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【微博动态】元素列表信息 | POST | `/api/portal/element/blogstatus` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【快捷入口】元素信息 | POST | `/api/portal/element/quickentry` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【我的协作】元素列表信息 | POST | `/api/portal/element/cooperation` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【我的协作】元素列表信息 | POST | `/api/portal/element/cooperationtab` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【我的协作】元素列表信息 | POST | `/api/portal/element/cooperation` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【我的邮件】元素列表信息 | POST | `/api/portal/element/mail` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【我的项目】元素列表信息 | POST | `/api/portal/element/projects` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【我的项目】元素列表信息 | POST | `/api/portal/element/projectstab` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【收藏元素】元素列表信息 | POST | `/api/portal/element/favourite` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【文档中心】元素数据 | POST | `/api/portal/element/newstab` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【文档中心】元素数据 | POST | `/api/portal/element/news` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【文档内容】元素列表信息 | POST | `/api/portal/element/doccontent` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【新建流程】元素信息 | POST | `/api/portal/element/addwftab` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【新建流程】元素信息 | POST | `/api/portal/element/addwf` | [门户管理_02.md](门户管理_02.md) |
| 获取门户【日历日程】元素列表信息 | POST | `/api/portal/element/mycalendar` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【最新会议】元素列表信息 | POST | `/api/portal/element/newmeeting` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【最新客户/未读文档】元素列表信息 | POST | `/api/portal/element/view` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【期刊中心】元素列表信息 | POST | `/api/portal/element/magazine` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【流程中心】元素数据 | POST | `/api/portal/element/workflowtab` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【流程中心】元素数据 | POST | `/api/portal/element/workflow` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【自定义菜单】元素列表信息 | POST | `/api/portal/element/custommenu` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【自定义页面】元素列表信息 | POST | `/api/portal/element/custompagetab` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【自定义页面】元素列表信息 | POST | `/api/portal/element/custompage` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【视频元素】元素列表信息 | POST | `/api/portal/element/video` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【通讯录】元素信息列表 | POST | `/api/portal/element/contacts` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【通讯录】元素信息列表 | POST | `/api/portal/element/contactstab` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【集成登录】元素信息 | POST | `/api/portal/element/outtersys` | [门户管理_03.md](门户管理_03.md) |
| 获取门户【音频元素】元素列表信息 | POST | `/api/portal/element/audio` | [门户管理_03.md](门户管理_03.md) |
| 获取门户菜单 | GET | `/api/portal/menu/getPortalMenu` | [门户管理_03.md](门户管理_03.md) |
| 设置我的主题字体大小 | POST | `/api/portal/themeCenter/setMyFontSize` | [门户管理_03.md](门户管理_03.md) |
