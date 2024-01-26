import React, { useState } from 'react'
import { ToastContainer, toast } from 'react-toastify';
import axios from 'axios';
import 'react-toastify/dist/ReactToastify.css';
const QueryForm = () => {
const [isResponse,setIsResponse]=useState(false);
const [limit,setLimit]=useState(5);
const [query,setQuery]=useState("");
const [response,setResponse]=useState("")

const fetchResponse = async(e) =>{
if(query===""){
toast.error("Please enter Query to Proceed");
}
else{
    
    setIsResponse(false);
    try {
        axios.get(`http://127.0.0.1:5000/query?tokenId=asdsad&query=${query}&limit=${limit}`)
        .then(function (response) {
            setIsResponse(true);
        
            setResponse(response.data);
            })
    }
    catch (error) {
        toast.error("Unable to fetch Response, Please try again !!")
        console.log(error)
    }
}
}


  return (
    <div className='w-full justify-center flex'>
        <ToastContainer/>
        <div className='w-3/4 max-sm:w-5/6 m-5 p-3 flex flex-col  rounded-xl border-solid border-2 border-yellow-400'>
            <label className='text-xl mt-3'>Enter Query :</label>
            <div className='flex justify-center my-3'>
            <input value={query} onChange={(e)=>{setQuery(e.target.value)}} className='w-3/4 max-sm:w-full bg-slate-800 p-2 rounded text-xl'></input>
            </div>
<div className='flex max-sm:flex-col justify-center'>
            <label className='text-xl flex justify-start mt-4 mx-5'>Limit Response to :</label>
            <div className='flex justify-center my-3'>
            <input  type='number' value={limit} onChange={(e)=>{
                if(e.target.value>=1){
                setLimit(e.target.value)}}}  className=' bg-slate-800 p-2 max-sm:w-full rounded text-xl'></input>
            </div>
            </div>
            <div>
                <button onClick={fetchResponse} className='px-4 py-3 mt-5 hover:bg-black border-2  border-gray-800 text-xl rounded-xl bg-slate-800'>Submit</button>
            </div>
            {
                isResponse&&
                <div>
                    <input value={response} type='text' disabled={true} className='p-2 text-xl max-sm:w-full mt-7 w-3/4 bg-slate-800 rounded min-h-48 mb-5'></input>
                </div>
            }
        </div>
    </div>
  )
}

export default QueryForm