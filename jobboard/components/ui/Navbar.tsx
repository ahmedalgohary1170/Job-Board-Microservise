import Link from "next/link"
import { Button } from "@/components/ui/button"

import { ModeToggle } from "../Togglebutton"


function NavBar(){
    return(
        <div className="flex items-center justify-between py-5 px-5 border-b-4">

            <Link href="/">
            <span>JobBourd</span>
            </Link>

            <div className="flex">
                <Button className="mr-2">
                    <Link href='/'>Login</Link>
                </Button>
                < ModeToggle />
            </div>
   
        </div>
    )
}


export default NavBar 