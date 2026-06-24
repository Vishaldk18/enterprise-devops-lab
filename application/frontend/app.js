async function loadData() {
 
    try {
 
        const healthResponse =
            await fetch("/api/health");
 
        const healthData =
            await healthResponse.json();
 
        document.getElementById("status").innerText =
            healthData.status;
 
        document.getElementById("redis").innerText =
            healthData.redis;
 
        document.getElementById("environment").innerText =
            healthData.environment;
 
        document.getElementById("version").innerText =
            healthData.version;
 
        const countResponse =
            await fetch("/api/visitor-count");
 
        const countData =
            await countResponse.json();
 
        document.getElementById("hostname").innerText =
            countData.hostname;
 
        document.getElementById("count").innerText =
            countData.count;
 
    }
    catch(error) {
 
        console.error(error);
 
        document.getElementById("status").innerText =
            "Backend Unreachable";
    }
}
 
loadData();
