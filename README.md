# code name - Hawthorn ( irl REESTR SERVICE )

  description:

* * *

## Packets for reestr

  description:

### query for `/searching`

  description:

  searching: {
   required id: uint32
   required serarch_type: string
   repeated querys: query
  }

  query: {
   optional сadastr_id: uint32
   required region: string
   optional district: string
   optional populated_area: string
   required street: string
   required street_name: string
   required house_number: string
   required apartment: string
  }

### answer for `/searching`

  description:

  answer: {
      required id: uint32
      repeated search_uid: uint32
  }

## structs for reestr base

### struct of search object

  description: maby separate

  realty : {
      required search_uid: uint32
      required date_request: yyyy-dd-MMThh:mm:ss (or some like this)
      required date_response: yyyy-dd-MMThh:mm:ss (or some like this)
      optional сadastr_id: uint32
      required region: string
      optional district: string
      optional populated_area: string
      required street: string
      required street_name: string
      required house_number: string
      required apartment: string
      required zip_url:string
    }

### struct of the task of request

  description:

  task: {
      required task_uid: uint32
      repeated realtys: realty
  }

  ========================Selenium======================
  login by token, step first:
  url: <https://rosreestr.ru/wps/portal/p/cc_present/ir_egrn>
  token: c5793610-b33b-476f-bebf-53a0f1366383

  =====================================================
