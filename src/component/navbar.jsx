import React from 'react'
import logo from '../rbilogo.png'
import { IoMdInformationCircleOutline } from "react-icons/io";

const Navbar = () => {
  return (
    <div className='bg-yellow-400 w-full px-5 flex justify-between flex-row m-auto h-16'>
        <img src={logo} alt='logo'></img>
        <h1 className='flex my-4 font-bold text-xl text-gray-800'>RBI Chatbot</h1>
<div className='py-3 text-gray-800'><IoMdInformationCircleOutline size={40}/></div>
    </div>
  )
}

export default Navbar