/**
 * 泛微 Ecology 9 工作流程 (Workflow) 对接实战脚本 (Node.js)
 * 涵盖流程：
 * 1. 查询可发起的流程类型与流程定义
 * 2. 构造主表与明细表数据，调用 doCreateRequest 创建并流转新流程
 * 3. 查询当前用户的待办列表 (getToDoWorkflowRequestList)
 * 4. 查询流程流转日志与签字意见 (getRequestLog)
 */

const EcologyClient = require('../scripts/ecology_token_client');

// 1. 初始化客户端
const client = new EcologyClient({
  baseUrl: 'http://oa.yourcompany.com:8088',
  appId: 'ERP_INTEGRATION_01',
  defaultUserId: '1' // 系统管理员或指定员工ID
});

async function runWorkflowDemo() {
  try {
    console.log('=== 步骤 1：查询待办流程列表 ===');
    const todoRes = await client.request({
      path: '/api/workflow/paService/getToDoWorkflowRequestList',
      method: 'POST',
      data: {
        pageNo: '1',
        pageSize: '10'
      }
    });
    console.log('待办列表返回结果:', JSON.stringify(todoRes, null, 2));

    console.log('\n=== 步骤 2：创建并提交一条新流程 ===');
    // 构造流程表单数据
    const createPayload = {
      workflowId: '102', // 泛微流程定义ID
      requestName: `采购申请单 - ${new Date().toISOString().slice(0, 10)} - 第三方自动发起`,
      isnextflow: '1',    // 1: 直接流转到下一节点; 0: 保存为草稿
      mainData: [
        { fieldName: 'sqr', fieldValue: '1' },         // 申请人ID (HrmResource)
        { fieldName: 'sqrq', fieldValue: '2026-08-14' },// 申请日期
        { fieldName: 'cgje', fieldValue: '5800.00' },   // 采购总金额
        { fieldName: 'bz', fieldValue: 'ERP系统自动推单采购' }
      ],
      detailData: [
        {
          tableDBName: 'formtable_main_102_dt1', // 明细表1名
          rows: [
            [
              { fieldName: 'wpmc', fieldValue: '服务器固态硬盘 2TB' },
              { fieldName: 'sl', fieldValue: '4' },
              { fieldName: 'dj', fieldValue: '950.00' },
              { fieldName: 'je', fieldValue: '3800.00' }
            ],
            [
              { fieldName: 'wpmc', fieldValue: '千兆交换机 24口' },
              { fieldName: 'sl', fieldValue: '1' },
              { fieldName: 'dj', fieldValue: '2000.00' },
              { fieldName: 'je', fieldValue: '2000.00' }
            ]
          ]
        }
      ]
    };

    const createRes = await client.request({
      path: '/api/workflow/paService/doCreateRequest',
      method: 'POST',
      data: createPayload
    });

    console.log('创建流程返回:', JSON.stringify(createRes, null, 2));

    if (createRes.data && createRes.data.requestId) {
      const newRequestId = createRes.data.requestId;
      console.log(`\n=== 步骤 3：查询新创建流程 [${newRequestId}] 的流转操作人信息 ===`);
      const operatorRes = await client.request({
        path: '/api/workflow/paService/getRequestOperatorInfo',
        method: 'GET',
        params: { requestId: newRequestId }
      });
      console.log('流转节点与操作人:', JSON.stringify(operatorRes, null, 2));
    }
  } catch (err) {
    console.error('流程接口调用异常:', err);
  }
}

// 执行
runWorkflowDemo();
