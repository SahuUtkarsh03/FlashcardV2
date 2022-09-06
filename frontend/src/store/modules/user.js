const state ={
    errMsg: null,
    token:null
};

const getters={
    getErrMsg: (state) => state.errMsg,
    getToken: (state) => state.token
};

const actions={
    Token: async (context,token)=> context.commit('setToken',token),
    ErrorMsg: async (context,msg)=> context.commit('setErrMsg',msg),
    clearToken: async (context)=> context.commit('clearToken')
};

const mutations={
    setErrMsg: (state, errMsg) => state.errMsg=errMsg,
    setToken: (state,token)=>state.token=token,
    clearToken: (state)=>state.token=null
};

export default {
    state,
    getters,
    actions,
    mutations
};
