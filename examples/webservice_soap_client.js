/**
 * 泛微 Ecology WebService (SOAP) 客户端调用示例 (Node.js)
 * 无需外部大型 SOAP 框架，基于原生 HTTP 发送 SOAP XML 报文
 */

const http = require('http');
const { URL } = require('url');

class WeaverSoapClient {
  constructor(baseUrl) {
    this.baseUrl = baseUrl.replace(/\/+$/, '');
  }

  sendSoapRequest(serviceName, actionName, xmlBody) {
    return new Promise((resolve, reject) => {
      const urlStr = `${this.baseUrl}/services/${serviceName}`;
      const urlObj = new URL(urlStr);

      const headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': actionName || '',
        'Content-Length': Buffer.byteLength(xmlBody)
      };

      const req = http.request(
        {
          hostname: urlObj.hostname,
          port: urlObj.port || 80,
          path: urlObj.pathname,
          method: 'POST',
          headers
        },
        (res) => {
          let chunks = [];
          res.on('data', (c) => chunks.push(c));
          res.on('end', () => {
            const responseText = Buffer.concat(chunks).toString('utf8');
            resolve({ statusCode: res.statusCode, data: responseText });
          });
        }
      );

      req.on('error', (err) => reject(err));
      req.write(xmlBody);
      req.end();
    });
  }

  /**
   * 通过 WorkflowService 发起一条新流程
   */
  async createWorkflowRequest({ workflowId, requestName, creatorId = '1', mainFields = {} }) {
    let fieldsXml = '';
    for (const [k, v] of Object.entries(mainFields)) {
      fieldsXml += `
        <web:workflowRequestTableField>
          <web:fieldName>${k}</web:fieldName>
          <web:fieldValue>${v}</web:fieldValue>
          <web:viewFlag>true</web:viewFlag>
          <web:editFlag>true</web:editFlag>
        </web:workflowRequestTableField>`;
    }

    const soapXml = `
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservices.workflow.weaver">
   <soapenv:Header/>
   <soapenv:Body>
      <web:doCreateWorkflowRequest>
         <web:in0>
            <web:creatorId>${creatorId}</web:creatorId>
            <web:requestName>${requestName}</web:requestName>
            <web:requestLevel>0</web:requestLevel>
            <web:workflowBaseInfo>
               <web:workflowId>${workflowId}</web:workflowId>
            </web:workflowBaseInfo>
            <web:workflowMainTableInfo>
               <web:requestProperties>${fieldsXml}
               </web:requestProperties>
            </web:workflowMainTableInfo>
         </web:in0>
         <web:in1>${creatorId}</web:in1>
      </web:doCreateWorkflowRequest>
   </soapenv:Body>
</soapenv:Envelope>`.trim();

    return await this.sendSoapRequest('WorkflowService', 'doCreateWorkflowRequest', soapXml);
  }
}

module.exports = WeaverSoapClient;

if (require.main === module) {
  console.log('泛微 SOAP WebService 客户端工具类加载成功');
}
