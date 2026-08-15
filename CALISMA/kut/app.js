// Evrenakı - Kut Simülasyonu
// 3B Sabit ve 4B Salınımlı Yan Yana Gösterim

let scene, camera, renderer;
// 3D Model
let kut3D, wire3D;
// 4D Model
let kut4D, wire4D;

let baseSpeed = 0.05;
let speedMultiplier = 1.0;

init();
animate();

function init() {
    scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x050510, 0.02);

    camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
    // Kamerayı biraz geriye alalım ki iki şekil de sığsın
    camera.position.z = 10;
    camera.position.y = 2;
    camera.lookAt(0, 0, 0);

    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    document.body.appendChild(renderer.domElement);

    const ambientLight = new THREE.AmbientLight(0x222233);
    scene.add(ambientLight);

    // Sol Işık (3D için Mavi)
    const lightLeft = new THREE.PointLight(0x00f0ff, 2, 50);
    lightLeft.position.set(-6, 5, 5);
    scene.add(lightLeft);

    // Sağ Işık (4D için Pembe)
    const lightRight = new THREE.PointLight(0xff00e5, 2, 50);
    lightRight.position.set(6, -5, -5);
    scene.add(lightRight);

    // Ortak Geometri (Basık Küre)
    const geometry = new THREE.SphereGeometry(2, 64, 64);
    geometry.scale(1, 0.6, 1); 

    // === SOL: 3B SABİT KUT ===
    const material3D = new THREE.MeshPhysicalMaterial({
        color: 0x111122, emissive: 0x001a33, roughness: 0.1, metalness: 0.8,
        clearcoat: 1.0, transparent: true, opacity: 0.9
    });
    kut3D = new THREE.Mesh(geometry, material3D);
    kut3D.position.x = -3.5;
    scene.add(kut3D);

    const wireMat3D = new THREE.MeshBasicMaterial({ color: 0x00f0ff, wireframe: true, transparent: true, opacity: 0.15 });
    wire3D = new THREE.Mesh(geometry, wireMat3D);
    wire3D.scale.set(1.02, 1.02, 1.02);
    wire3D.position.x = -3.5;
    scene.add(wire3D);

    // Sol Eksen
    const axisGeo = new THREE.CylinderGeometry(0.02, 0.02, 4, 16);
    const axisMat = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.3 });
    const axisL = new THREE.Mesh(axisGeo, axisMat);
    axisL.position.x = -3.5;
    scene.add(axisL);

    // === SAĞ: 4B SALINIMLI KUT ===
    const material4D = new THREE.MeshPhysicalMaterial({
        color: 0x111122, emissive: 0x330022, roughness: 0.1, metalness: 0.8,
        clearcoat: 1.0, transparent: true, opacity: 0.9
    });
    kut4D = new THREE.Mesh(geometry, material4D);
    kut4D.position.x = 3.5;
    scene.add(kut4D);

    const wireMat4D = new THREE.MeshBasicMaterial({ color: 0xff00e5, wireframe: true, transparent: true, opacity: 0.25 });
    wire4D = new THREE.Mesh(geometry, wireMat4D);
    wire4D.scale.set(1.02, 1.02, 1.02);
    wire4D.position.x = 3.5;
    scene.add(wire4D);

    // Sağ Eksen
    const axisR = new THREE.Mesh(axisGeo, axisMat);
    axisR.position.x = 3.5;
    scene.add(axisR);


    // UI Olayları
    window.addEventListener('resize', onWindowResize);
    document.getElementById('speedSlider').addEventListener('input', (e) => {
        speedMultiplier = parseFloat(e.target.value);
    });
    document.getElementById('toggleWireframe').addEventListener('click', () => {
        wire3D.visible = !wire3D.visible;
        wire4D.visible = !wire4D.visible;
    });
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
    requestAnimationFrame(animate);
    let time = Date.now() * 0.001;

    // Her ikisi de ekvatordan hızla döner
    let rotationAmount = baseSpeed * speedMultiplier;
    kut3D.rotation.y += rotationAmount;
    wire3D.rotation.y += rotationAmount;
    
    kut4D.rotation.y += rotationAmount;
    wire4D.rotation.y += rotationAmount;

    // Yüzme efekti
    const float = Math.sin(time) * 0.1;
    kut3D.position.y = float;
    wire3D.position.y = float;
    kut4D.position.y = float;
    wire4D.position.y = float;

    // 4B BOYUTSAL SALINIM (Dimensional Oscillation)
    // 4D olan nesne kendi merkezinde nabız gibi şişip iner (boyutsal değişim).
    // Evrenakı'da temel yapılar devinemez, ancak 4. boyuta doğru salınırlar.
    let scalePulse = 1.0 + Math.sin(time * 5 * speedMultiplier) * 0.15;
    kut4D.scale.set(scalePulse, scalePulse, scalePulse);
    wire4D.scale.set(scalePulse * 1.02, scalePulse * 1.02, scalePulse * 1.02);

    renderer.render(scene, camera);
}
