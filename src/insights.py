from src.jobs import read

# Requisito 2


def get_unique_job_types(path):
    file_jobs = read(path)
    list_jobs = []
    for job in file_jobs:
        if job["job_type"] not in list_jobs:
            list_jobs.append(job["job_type"])

    return list_jobs

    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    # return []


# Requisito 6
def filter_by_job_type(jobs, job_type):
    filter_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)

    return filter_jobs
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    # return []


# Requisito 3
def get_unique_industries(path):
    file_jobs = read(path)
    list_industries = []
    for job in file_jobs:
        if job["industry"] not in list_industries:
            if job["industry"] != "":
                list_industries.append(job["industry"])
    return list_industries

    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    # return []


# Requisito 7
def filter_by_industry(jobs, industry):
    filter_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)

    return filter_industry
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    # return []


# Requisito 4
def get_max_salary(path):
    file_jobs = read(path)
    list_max_salary = []
    for job in file_jobs:
        if job["max_salary"] not in list_max_salary:
            if job["max_salary"] != "" and job["max_salary"].isdigit():
                list_max_salary.append(int(job["max_salary"]))
                max_salary = max(list_max_salary)

    return max_salary
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    pass


# Requisito 5
def get_min_salary(path):
    file_jobs = read(path)
    list_min_salary = []
    for job in file_jobs:
        if job["min_salary"] not in list_min_salary:
            if job["min_salary"] != "" and job["min_salary"].isdigit():
                list_min_salary.append(int(job["min_salary"]))
                min_salary = min(list_min_salary)

    return min_salary
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


# Requisito 8
def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("value does not exist")
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("the value is not a valid number")
    elif int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("min_salary value is greater than max_salary value")
    elif type(salary) != int:
        raise ValueError("salary value is not a valid number")

    return salary in range(int(job["min_salary"]), int(job["max_salary"]))

    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
