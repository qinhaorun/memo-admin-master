<!--suppress ALL -->
<script setup lang="ts">


// var formValue = vueref({
//   avatar: {
//     loginemail: "",
//     avatarId: "",
//     fileUniqueName: "",
//     skeletonName: "",
//     defaultAnimationName: "",
//     defaultSkinName: "",
//     avatar_name: "",
//     profile_photo: "",
//     profile_posture: ""
//
//   },
//
// });



// var formValuePosture = vueref({
//   posture: {
//     uploaderid: '',
//     avatarId: '',
//     posture_name: '',
//     posture_name_disp: '',
//     posture_preview_url: ''
//   },
// });


// var formValueSkin = vueref({
//   skin: {
//     uploaderid: '',
//     avatarId: '',
//     acc_name: '',
//     acc_type: '',
//     acc_name_disp: '',
//     acc_url: '',
//   },
// });

var rules = {
  posture: {
    aid: {
      required: true,
      message: 'Uploader ID',
      trigger: 'blur',
      placeholder: '_system_loader'
    },
    posture_name: {
      required: true,
      message: 'Avatar ID',
      trigger: 'blur',
    },
    posture_name_disp: {
      required: true,
      message: 'Posture Name',
      trigger: 'blur',
    },
    postureid: {
      required: true,
      message: 'Posture Disp Name',
      trigger: 'blur',
    },
    posture_preview_url: {
      required: true,
      message: 'Preview Url',
      trigger: 'blur',
    },
    rec_index: {
      required: true,
      message: 'rec_index',
      trigger: 'blur',
    },
  },
  avatar: {
    uploaderid: {
      required: true,
      message: 'Uploader ID',
      trigger: 'blur',
      placeholder: '_system_loader'
    },
    avatarId: {
      required: true,
      message: 'Avatar ID',
      trigger: 'blur',
    },
    fileUniqueName: {
      required: true,
      message: 'fileUniqueName',
      trigger: 'blur',
    },
    skeletonName: {
      required: true,
      message: 'Skeleton Name',
      trigger: 'blur',
    },
    defaultAnimationName: {
      required: true,
      message: 'Default Animation',
      trigger: 'blur',
    },
    defaultSkinName: {
      required: true,
      message: 'Default Skin',
      trigger: 'blur',
    },
    avatar_name: {
      required: true,
      message: 'Avatar Disp Name',
      trigger: 'blur',
    },
    profile_photo_url: {
      required: true,
      message: 'Profile Photo Url',
      trigger: 'blur',
    },
    profile_posture_url: {
      required: true,
      message: 'Posture Url',
      trigger: 'blur',
    },
  },
  skin: {
    uploaderid: {
      required: true,
      message: 'Uploader ID',
      trigger: 'blur',
      placeholder: '_system_loader'
    },
    avatarId: {
      required: true,
      message: 'Avatar ID',
      trigger: 'blur',
    },
    acc_name: {
      required: true,
      message: 'Skin Name',
      trigger: 'blur',
    },
    acc_type: {
      required: true,
      message: 'Skin Type',
      trigger: 'blur',
    },
    acc_name_disp: {
      required: true,
      message: 'Skin Disp Name',
      trigger: 'blur',
    },
    acc_url: {
      required: true,
      message: 'Skin Preview Url',
      trigger: 'blur',
    },
  }
};




</script>

<template>

<!-- all avatars are uniquely identified by aid/avatarId, and has a fileUniqueName.  -->
<!-- can get all meta data by /get_existing_aid_meta -->


<!-- 1. meta data, fields see api /update_avatar_metadata-->
<NH2>Avatar Meta Data</NH2>
 <NForm
    :model="formValue"
    :rules="rules"
    ref="formRef"
    require-mark-placement="right-hanging"
    label-width="auto"
  >
    <NFormItem label="Login Email" path="avatar.loginemail">
      <NInput v-model:value="formValue.avatar.loginemail" placeholder= "loginemail" />
    </NFormItem>
    <NFormItem label="Avatar ID" path="avatar.avatarId">
      <NInput placeholder="Avatar ID" v-model:value="formValue.avatar.avatarId" />
    </NFormItem>

    <NFormItem label="File UniqueName" path="avatar.fileUniqueName">
      <NInput placeholder="fileUniqueName" v-model:value="formValue.avatar.fileUniqueName" />
    </NFormItem>

    <NFormItem label="Default SkeletonName" path="avatar.skeletonName">
      <NInput placeholder="default" v-model:value="formValue.avatar.skeletonName" />
    </NFormItem>

    <NFormItem label="Default AnimationName" path="avatar.defaultAnimationName">
      <NInput placeholder="default" v-model:value="formValue.avatar.defaultAnimationName" />
    </NFormItem>

    <NFormItem label="Default SkinName" path="avatar.defaultSkinName">
      <NInput placeholder="default" v-model:value="formValue.avatar.defaultSkinName" />
    </NFormItem>

    <NFormItem label="Avatar AvatarName" path="avatar.avatar_name">
      <NInput placeholder="AvatarName" v-model:value="formValue.avatar.avatar_name" />
    </NFormItem>


<!--  TODO make draggable -->
    <NFormItem label="Profile Photo" path="avatar.profile_photo">
      <NInput placeholder="" v-model:value="formValue.avatar.profile_photo" />
    </NFormItem>

    <NFormItem label="Posture Photo" path="avatar.profile_posture">
      <NInput placeholder="" v-model:value="formValue.avatar.profile_posture" />
    </NFormItem>

<!-- TODO call backend -->
    <NFormItem>
      <NButton @click="handleValidateClickMeta(formValue.avatar)" attr-type="button">Confirm</NButton>
    </NFormItem>
  </NForm>

<!-- 2. upload corresponding files. params see backend /upload_avatar_bundle -->
  <NH2>Avatar Upload</NH2>
  <NUpload multiple 
    @drop="onUpload"
    @change="onUpload"
    @dragend="onUpload"
    >
    <NUploadDragger style="background: white;" >
      <div>
        <NIcon size="200" :depth="3">
          <ArrowUpload24Regular />
        </NIcon>
      </div>
      <NText style="font-size: 16px"
        >Click or drag files here to upload</NText
      >
    </NUploadDragger>
  </NUpload>

<!-- upload all files to db.  -->
  <NButton
    @click="clickUpload"> Upload</NButton>


<!-- should get return value from parsing the files just uploaded. -->
  <!-- 3. and show pages to fill in /update_avatar_pospreview -->  
  

<NH2>Avatar Postures</NH2>
<!-- TODO should display postures default name here -->
<!-- Should make multiple -->
<ul id="postures">
  <li v-for="item in this.Formdatas" v-bind:key="item">

 <NForm
    inline
    :model="Formdatas"
    :rules="rules"
    ref="formRef"
    require-mark-placement="right-hanging"
    label-width="auto">
   <NFormItem label="loginemail" path="posture.postureid">
     <NInput placeholder="" v-model:value="formValue.avatar.loginemail" />
   </NFormItem>
    <NFormItem label="avatarId" path="posture.aid">
      <NInput v-model:value="item.aid" placeholder= "" />
    </NFormItem>
    <NFormItem label="posture_name" path="posture.posture_name">
      <NInput placeholder="" v-model:value="item.posture_name" />
    </NFormItem>

    <NFormItem label="posture_name_disp" path="posture.posture_name_disp">
      <NInput placeholder="" v-model:value="item.posture_name_disp" />
    </NFormItem>

    <NFormItem label="posture_preview_url" path="posture.posture_preview_url">
      <NInput placeholder="" v-model:value="item.posture_preview_url" />
    </NFormItem>



<!-- TODO call backend -->
    <NFormItem>
      <NButton @click="showModal([formValue.avatar.loginemail,item.aid,item.posture_name,item.posture_name_disp,item.posture_preview_url])" attr-type="button">验证</NButton>
    </NFormItem>
  </NForm>

    </li>
</ul>


  
<!-- 4. and show pages to fill in Skin preview /update_avatar_skinpreview -->
<NH2>Avatar Skins</NH2>

  <!-- <NText label="Uploader ID" path="skin.uploaderid">
      <NInput v-model:value="formValue.skin.uploaderid" placeholder= "Uploader ID" />
    </NText>
    <NText label="Avatar ID" path="skin.avatarId">
      <NInput placeholder="Avatar ID" v-model:value="formValue.skin.avatarId" />
    </NText> -->


<!-- TODO Should be multiple -->
<ul id="skins">
  <li v-for="item in this.skinItems" v-bind:key="item">
    <NForm
    inline
    :model="skinItems"
    :rules="rules"
    ref="formRef"
    require-mark-placement="right-hanging"
    label-width="auto"
  >

    <NFormItem label="loginemail" path="skin.acc_name">
      <NInput placeholder="" v-model:value="formValue.avatar.loginemail" />
    </NFormItem>

    <NFormItem label="avatarId" path="skin.acc_name_disp">
      <NInput placeholder="" v-model:value="item.aid" />
    </NFormItem>
      <NFormItem label="acc_name" path="skin.accid">
        <NInput placeholder="" v-model:value="item.acc_name" />
      </NFormItem>
    <NFormItem label="acc_type" path="skin.acc_type">
      <NInput placeholder="" v-model:value="item.acc_type" />
    </NFormItem>
      <NFormItem label="acc_name_disp" path="skin.aid">
        <NInput placeholder="" v-model:value="item.acc_name_disp" />
      </NFormItem>
<!-- TODO make draggable -->
    <NFormItem label="acc_url" path="skin.acc_url">
      <NInput placeholder="" v-model:value="item.acc_url" />
    </NFormItem>




<!-- TODO call backend -->
    <NFormItem>
      <NButton @click="handleValidateClickSkins([formValue.avatar.loginemail,item.aid,item.acc_name,item.acc_type,item.acc_name_disp,item.acc_url])" attr-type="button">Confirm</NButton>
    </NFormItem>

  </NForm>

  </li>
</ul>
<!--  模态框-->




<!-- -->
</template>


<script lang="ts">
import {NModal,NDataTable,NTable,NText, NForm, NFormItem, NInput, NButton, NUpload, NUploadDragger, NIcon, NH2, UploadFileInfo, UploadProps } from "naive-ui";
import { ArrowUpload24Regular } from "@vicons/fluent";
import { getStorage, ref, uploadBytesResumable, getDownloadURL, list } from "firebase/storage";
import Vue, { computed } from 'vue';
import { useMessage } from 'naive-ui';
import { Emitter } from "mitt";
// import {defineComponent, ref as vueref} from 'vue';
import {defineComponent} from 'vue'
import firebase from "firebase/app";
import axios from "axios";

export default defineComponent({
  components:{NDataTable,NTable},
  setup () {},
  data(){
    return {
      // 1. for meta data
      formValue:{
        avatar: {
          loginemail: "",
          avatarId: "",
          fileUniqueName: "",
          skeletonName: "",
          defaultAnimationName: "",
          defaultSkinName: "",
          avatar_name: "",
          profile_photo: "",
          profile_posture: ""

        },
      },
      // 2. for upload
      myfilestatus: false,
      fileMapJson : {} as any,
      // 3. for postures
      posItems: [1,2,3,4,5,6] as any,
      // 4. for skins
      skinItems: [{
        acc_name:"",
        acc_name_disp:"",
        acc_type:"",
        acc_url:"",
        accid:"",
        aid:"",
        rec_index:"",
      }] as any,

      Formdatas:[{
        aid:"",
        posture_name: '',
        posture_name_disp: "",
        posture_preview_url: '',
      }],
      datajson3 :{
        "loginemail": "_sys",
        "avatarId": 1,
        "posture_name": "1",
        "posture_name_disp": "posture desp",
        "posture_preview_url": ""
      },
      datajson4:{
        "loginemail": "_sys",
        "avatarId": 1,
        "acc_name": "cap/badgelol",
        "acc_type": "posture desp",
        "acc_name_disp": "acc disp",
        "acc_url" : ""
      }
    }
  },
  mounted(){
    console.log("mounted");

  },
  methods : {

    // 1. for creating meta data. 
    handleValidateClickMeta(input: any){
      console.log(input)
      console.log(JSON.stringify(input))
      axios({
        url:"https://memology-demo.herokuapp.com/create_avatar_metadata",
        method:"post",
        headers:{
          'Content-Type':'application/json'
        },
        data:JSON.stringify(input)
      }).then((res)=>{
        if (res.data.status_code === 200){
          // success
          alert(res.data.message)
        }else {
          // 已经存在
          alert(res.data.message)
        }
      })
    },
    // 3. postures
    showModal(input:any){

      this.datajson3.loginemail = input[0]
      this.datajson3.avatarId = input[1]
      this.datajson3.posture_name = input[2]
      this.datajson3.posture_name_disp = input[3]
      this.datajson3.posture_preview_url = input[4]

      axios({
        url:"https://memology-demo.herokuapp.com/update_avatar_pospreview",
        method:"post",
        headers:{
          'Content-Type':'application/json'
        },
        data:JSON.stringify(this.datajson3)
      }).then((res)=>{

        if (res.data.status_code === 200){
          alert(res.data.message)
        }else {
          alert(res.data.message)
        }
      })
    },
    // 4. skins
    handleValidateClickSkins(input:any){

      this.datajson4.loginemail = input[0]
      this.datajson4.avatarId = input[1]
      this.datajson4.acc_name = input[2]
      this.datajson4.acc_type = input[3]
      this.datajson4.acc_name_disp = input[4]
      this.datajson4.acc_url = input[5]
      axios({
        url:"https://memology-demo.herokuapp.com/update_avatar_skinpreview",
        method:"post",
        headers:{
          'Content-Type':'application/json'
        },
        data:JSON.stringify(this.datajson4)
      }).then((res)=>{

        if (res.data.status_code === 200){
          alert(res.data.message)
        }else {
          alert(res.data.message)
        }
      })
    },

    // 2.  For avatar upload
    // below is just a sample
    async clickUpload() {

        console.log(this.myfilestatus);
        this.myfilestatus = true;
        // upload list of filename - url pair to server
        console.log( "printing file list" );
        let requestJson : any  = {}; 
        requestJson["loginemail"] = this.formValue.avatar.loginemail;

        requestJson["avatarId"] = this.formValue.avatar.avatarId;
        requestJson["fileUniqueName"] = this.formValue.avatar.fileUniqueName;
        requestJson["urlList"] = this.fileMapJson;
      console.log("requestJson"+JSON.stringify(requestJson))
        await axios({
          method:"post",
          url:"https://memology-demo.herokuapp.com/upload_avatar_bundle",
          headers:{
            'Content-Type':'application/json'
          },
          data:JSON.stringify(requestJson)
        }).then((res)=>{
          console.log("数据加载成功"+JSON.stringify(res.data))

          this.Formdatas = res.data.data.ret_pos
          this.skinItems = res.data.data.ret_acc
        })
        // const response = await axios.post("https://memology-demo.herokuapp.com/upload_avatar_bundle", requestJson);


    },


  async onUpload (uploadProps: UploadProps){
      
      this.myfilestatus = false;
      console.log("upload my");
      console.log( uploadProps.fileList );
      const storage = await getStorage();

      this.fileMapJson = {};

      uploadProps.fileList?.forEach( async(element) => {
        const filename : string|undefined = element.name ;
        const fileRef = ref(storage, filename);
        const fileAB  = await element.file?.arrayBuffer().then(
          async(buff) => {
            const uploadTask = uploadBytesResumable(fileRef, buff);
          uploadTask.on('state_changed', 
            (snapshot) => {
              const progress =  (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
              console.log('Upload is ' + progress + '% done');
              switch (snapshot.state) {
                case 'paused':
                  console.log('Upload is paused');
                  break;
                case 'running':
                  console.log('Upload is running');
                  break;
              }
            }, 
            (error) => {
              console.log(error);
            }, 
              async () => {
                await getDownloadURL(uploadTask.snapshot.ref).then((downloadURL) => {
                  console.log('File available at', downloadURL);
                  this.fileMapJson[filename] = downloadURL ;
                  console.log("this.fileMapJson"+JSON.stringify(this.fileMapJson))
                });
              }
          );
          }
        );
      });

    }

  }
})
</script>


