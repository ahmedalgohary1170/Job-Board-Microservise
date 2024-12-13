import JobsFilter from "@/components/jobs/jobsFilter"
import JobsList from "@/components/jobs/jobsList"


function JobListPage(){
    // logic


    //return
    return(
        <div>
            <h3> Job List </h3>
            <JobsList/>
            <JobsFilter/>
        </div>
    )

}

export default JobListPage