function pow(a,b){
    if(b==0){
        return 1
    }
    if(b==1){
        return a
    }
    else{
        return a*(pow(a,b-1))
    }
}